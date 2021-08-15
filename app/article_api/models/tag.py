from django.db import models
from article_api.models import Article


class Tag(models.Model):
    tag = models.CharField(
        max_length=50, unique=True, null=False, blank=False
    )  # Assuming tags are unique
    articles = models.ManyToManyField(Article)

    def __str__(self):
        return self.tag
