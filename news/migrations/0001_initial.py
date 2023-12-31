# Generated by Django 4.2.6 on 2023-10-28 03:46

from django.db import migrations, models
import news.models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="News",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("href", models.URLField()),
                ("img_src", models.URLField(blank=True, null=True)),
                ("article_title", models.CharField(max_length=255)),
                (
                    "article_description",
                    models.TextField(
                        blank=True, default=news.models.get_empty_string, null=True
                    ),
                ),
                (
                    "article_footer",
                    models.TextField(
                        blank=True, default=news.models.get_empty_string, null=True
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "ordering": ("-created_at",),
            },
        ),
    ]
