from rest_framework.views import APIView
from rest_framework.response import Response
from app.mongo import get_mongoo_client
from app.serializers.reservation import ReservationSerializer
from datetime import datetime, timedelta
from bson.objectid import ObjectId
from datetime import datetime


class ReservationView(APIView):
    def post(self, request):
        serializer = ReservationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        client = get_mongoo_client()
        variant = client.invdb.variants.find_one({"variant_id": data["variant_id"]})

        #chheck stock
        if not variant or variant.get("available", 0) < data["qty"]:
            return Response({"error": "Insufficient stock"}, status=409)

        #atomic hold(decrement available, increment reserved)
        client.invdb.variants.update_one(
            {"variant_id": data["variant_id"], "available": {"$gte": data["qty"]}},
            {"$inc": {"available": -data["qty"], "reserved": data["qty"]}}
        )

        #create reservation docss with TTL
        expires_at = datetime.utcnow() + timedelta(seconds=data.get("hold_secs", 600))
        reservation = {
            "variant_id": data["variant_id"],
            "qty": data["qty"],
            "status": "HOLD",
            "expires_at": expires_at,
            "client_token": data["client_token"],
            "created_at": datetime.utcnow()
        }
        client.invdb.reservations.insert_one(reservation)
        return Response({"status": "HOLD"}, status=201)


#confirm resertvation apii
class ReservationConfirmView(APIView):
    def post(self, request, reservation_id):
        client = get_mongoo_client()
        reservation = client.invdb.reservations.find_one({"_id": ObjectId(reservation_id)})
        if not reservation or reservation["status"] != "HOLD":
            return Response({"error": "Invalid reservation"}, status=400)

        #move reserved - sold
        client.invdb.variants.update_one(
            {"variant_id": reservation["variant_id"]},
            {"$inc": {"reserved": -reservation["qty"], "sold": reservation["qty"]}}
        )
        client.invdb.reservations.update_one(
            {"_id": ObjectId(reservation_id)},
            {"$set": {"status": "CONFIRMED"}, "$unset": {"expires_at": ""}}
        )
        return Response({"status": "CONFIRMED"})
    


#cancell api
class ReservationCancelView(APIView):
    def post(self, request, reservation_id):
        client = get_mongoo_client()
        reservation = client.invdb.reservations.find_one({"_id": ObjectId(reservation_id)})
        if not reservation or reservation["status"] != "HOLD":
            return Response({"error": "Invalid reservation"}, status=400)

        #release hold
        client.invdb.variants.update_one(
            {"variant_id": reservation["variant_id"]},
            {"$inc": {"reserved": -reservation["qty"], "available": reservation["qty"]}}
        )
        client.invdb.reservations.update_one(
            {"_id": ObjectId(reservation_id)},
            {"$set": {"status": "CANCELED"}, "$unset": {"expires_at": ""}}
        )
        return Response({"status": "CANCELED"})
    
#audit
def write_audit(actor, action, before, after, route, ip_hash):
    client = get_mongoo_client()
    audit = {
        "actor": actor,
        "action": action,
        "before": before,
        "after": after,
        "route": route,
        "ip_hash": ip_hash,
        "created_at": datetime.utcnow()
    }
    client.invdb.audits.insert_one(audit)