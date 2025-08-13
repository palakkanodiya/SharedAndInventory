from rest_framework import serializers

class AuditSerializer(serializers.Serializer):
    actor = serializers.CharField()
    action = serializers.CharField()
    before = serializers.DictField()
    after = serializers.DictField()
    route = serializers.CharField()
    created_at = serializers.DateTimeField()