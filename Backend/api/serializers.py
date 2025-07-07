from rest_framework import serializers
from .models import ShortURL

class ShortenSerializer(serializers.Serializer):
    url = serializers.URLField()
    shortcode = serializers.CharField(required=False)
    validity = serializers.IntegerField(required=False, default=30)  # in minutes
