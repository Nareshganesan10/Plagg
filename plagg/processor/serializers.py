from rest_framework import serializers

class FileSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=1000, allow_blank=True)
    file = serializers.FileField()