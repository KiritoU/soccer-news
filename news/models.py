from django.db import models

# Create your models here.


def get_empty_string():
    return ""


class News(models.Model):
    href = models.URLField(unique=True)
    img_src = models.URLField(blank=True, null=True)
    article_title = models.CharField(max_length=255)
    article_description = models.TextField(
        blank=True, null=True, default=get_empty_string
    )
    article_footer = models.TextField(blank=True, null=True, default=get_empty_string)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self) -> str:
        return f"{self.article_title}\t=> {self.href}"
