import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand, CommandError
from icecream import ic

from news.models import News


def get_article_img_src(article: BeautifulSoup) -> str:
    imgs = article.find_all("img")
    img_src = ""
    for img in imgs:
        if img.get("src", "") and not img_src:
            img_src = img.get("src")

    return img_src


def get_article_title(article: BeautifulSoup) -> str:
    header = article.find("header")
    article_title = header.text

    return article_title


def get_article_footer(article: BeautifulSoup) -> str:
    try:
        footer = article.find("footer")
        article_footer = footer.text

        return article_footer
    except:
        return ""


def get_article_description(article: BeautifulSoup) -> str:
    try:
        p = article.find("p")
        article_description = p.text

        return article_description
    except:
        return ""


def get_news_by_page(page: int):
    ic(page)
    url = f"https://www.90min.com/us/soccer-news?page={page}"

    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    articles = soup.find_all("article")
    ic(len(articles))

    for article in articles[::-1]:
        try:
            href = article.find("a").get("href")
            img_src = get_article_img_src(article)
            article_title = get_article_title(article)
            article_description = get_article_description(article)
            article_footer = get_article_footer(article)

            new, _ = News.objects.get_or_create(href=href)
            new.img_src = img_src
            new.article_title = article_title
            new.article_description = article_description
            new.article_footer = article_footer
            new.save()
            # ic(new)

        except Exception as e:
            ic(e)


class Command(BaseCommand):
    help = "Get all news"

    def handle(self, *args, **options):
        for page in range(174, 1, -1):
            get_news_by_page(page)
