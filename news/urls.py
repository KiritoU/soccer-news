from django.conf import settings
from django.contrib import admin
from django.urls import path

from .views import NewsListAPIView, NewsRetrieveAPIView

urlpatterns = [
    path("<int:pk>/", NewsRetrieveAPIView.as_view(), name="news-retrieve"),
    path("", NewsListAPIView.as_view(), name="news-list"),
]
