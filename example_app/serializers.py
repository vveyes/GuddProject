from rest_framework import serializers
from .models import TextID


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextID
        fields = ("uuid", "text", "created_at")
