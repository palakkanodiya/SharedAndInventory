from django.http import JsonResponse
from app.tasks import reconcile_backorders
from rest_framework.views import APIView
from rest_framework.response import Response
from app.mongo import get_mongoo_client
from app.serializers.admin import StockAdjustmentSerializer, ReconciliationTriggerSerializer
from app.tasks import reconcile_backorders


def trigger_reconciliation(request):
    reconcile_backorders.delay()
    return JsonResponse({'status': 'Reconciliation triggered'})


class AdjustStockView(APIView):
    def post(self, request):
        serializer = StockAdjustmentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        client = get_mongoo_client()
        client.invdb.variants.update_one(
            {"variant_id": data["variant_id"]},
            {"$inc": {"available": data["delta"]}}
        )
        return Response({"status": "Stock adjusted"}, status=200)

class TriggerReconciliationView(APIView):
    def post(self, request):
        serializer = ReconciliationTriggerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if serializer.validated_data["trigger"]:
            reconcile_backorders.delay()
            return Response({"status": "Reconciliation triggered"}, status=202)
        return Response({"status": "No action taken"}, status=200)
