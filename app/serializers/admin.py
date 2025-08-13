from rest_framework import serializers

class StockAdjustmentSerializer(serializers.Serializer):
    variant_id = serializers.CharField()
    delta = serializers.IntegerField()  # +ve or -ve change

class ReconciliationTriggerSerializer(serializers.Serializer):
    triger = serializers.BooleanField()