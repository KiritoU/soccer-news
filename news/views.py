from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import News
from .serializers import NewsDetailSerializer, NewsSerializer


class NewsListAPIView(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class NewsRetrieveAPIView(RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsDetailSerializer
