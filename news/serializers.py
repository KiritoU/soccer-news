import requests
from bs4 import BeautifulSoup
from icecream import ic
from rest_framework import serializers

from .models import News


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"


class NewsDetailSerializer(serializers.ModelSerializer):
    content = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = [
            "href",
            "img_src",
            "article_title",
            "article_description",
            "article_footer",
            "content",
        ]

    def get_content(self, new: News):
        href = new.href
        try:
            ic(f"Getting {href}...")
            response = requests.get(href, timeout=20)
            soup = BeautifulSoup(response.content, "html.parser")
            mmroot = soup.find("div", {"id": "mm-root"})
            mmroot__main = mmroot.find("main")
            article = mmroot__main.find("article")

            return str(article)

        except:
            return ""
