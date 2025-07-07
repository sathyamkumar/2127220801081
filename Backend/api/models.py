from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from datetime import timedelta

class ShortURL(models.Model):
    shortcode = models.CharField(max_length=20, unique=True)
    original_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    expiry = models.DateTimeField()
    click_count = models.IntegerField(default=0)

class ClickData(models.Model):
    shorturl = models.ForeignKey(ShortURL, on_delete=models.CASCADE, related_name='clicks')
    timestamp = models.DateTimeField(auto_now_add=True)
    referrer = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)