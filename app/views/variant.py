from rest_framework.views import APIView
from rest_framework.response import Response
from app.mongo import get_mongoo_client
from app.serializers.variant import VariantSerializer
from bson import ObjectId
from datetime import datetime


class VariantListView(APIView):
    def get(self, request):
        client = get_mongoo_client()
        variants = list(client.invdb.variants.find())
        for v in variants:
            if '_id' in v:
                v['_id'] = str(v['_id'])
        return Response(variants)


    def post(self, request):
        serializer = VariantSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)  #Validate input
        client = get_mongoo_client()
        client.invdb.variants.insert_one(serializer.validated_data)
        return Response({"status": "created"}, status=201)


class VariantDetailView(APIView):
    def get(self, request, variant_id):
        client = get_mongoo_client()
        variant = client.invdb.variants.find_one({"variant_id": variant_id})
        if variant and '_id' in variant:
            variant['_id'] = str(variant['_id'])
        return Response(variant)
    

def write_audit(actor, action, before, after, route):
    client = get_mongoo_client()
    audit = {
        "actor": actor,
        "action": action,
        "before": before,
        "after": after,
        "route": route,
        "created_at": datetime.utcnow()
    }
    client.invdb.audits.insert_one(audit)


