from django.urls import path
from .views import ShortenURL, ShortURLStats

urlpatterns = [
    path('shorten/', ShortenURL.as_view()),
    path('shorturls/<str:shortcode>', ShortURLStats.as_view()),
]
