from rest_framework import serializers

class ReservationSerializer(serializers.Serializer):
    variant_id = serializers.CharField()
    qty = serializers.IntegerField()
    client_token = serializers.CharField()
    hold_secs = serializers.IntegerField(required=False)