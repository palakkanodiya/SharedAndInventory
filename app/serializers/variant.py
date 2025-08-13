from rest_framework import serializers

class VariantSerializer(serializers.Serializer):
    variant_id = serializers.CharField()
    product_id = serializers.CharField()
    product_name = serializers.CharField()
    attrs = serializers.DictField()
    available = serializers.IntegerField()
    reserved = serializers.IntegerField()
    sold = serializers.IntegerField()
    backorderable = serializers.BooleanField()
    deleted_at = serializers.DateTimeField(required=False)