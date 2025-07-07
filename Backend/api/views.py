from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils.timezone import now
from django.shortcuts import get_object_or_404
from .models import ShortURL, ClickData
from .serializers import ShortenSerializer
from datetime import timedelta
import random, string

def generate_shortcode():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))

class ShortenURL(APIView):
    def post(self, request):
        serializer = ShortenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        shortcode = data.get('shortcode') or generate_shortcode()

        if ShortURL.objects.filter(shortcode=shortcode).exists():
            return Response({"error": "Shortcode already in use."}, status=400)

        expiry_time = now() + timedelta(minutes=data.get('validity', 30))
        shorturl = ShortURL.objects.create(
            shortcode=shortcode,
            original_url=data['url'],
            expiry=expiry_time
        )

        return Response({
            "shortLink": f"https://hostname:port/{shortcode}",
            "expiry": shorturl.expiry.isoformat().replace("+00:00", "Z")
        }, status=201)

class ShortURLStats(APIView):
    def get(self, request, shortcode):
        shorturl = get_object_or_404(ShortURL, shortcode=shortcode)

        if now() > shorturl.expiry:
            return Response({"error": "URL has expired."}, status=410)

        clicks = [
            {
                "timestamp": click.timestamp.isoformat(),
                "referrer": click.referrer,
                "location": click.location
            }
            for click in shorturl.clicks.all()
        ]

        return Response({
            "click_count": shorturl.click_count,
            "original_url": shorturl.original_url,
            "created_at": shorturl.created_at.isoformat(),
            "expiry": shorturl.expiry.isoformat(),
            "clicks": clicks
        })
