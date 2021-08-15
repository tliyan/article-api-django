from django.db import models


class Article(models.Model):
    # ID automatically added by Django upon creation, hence we don't add it as part of the model
    title = models.CharField(max_length=200, null=False, blank=False)
    date = models.DateField(null=False, blank=False)
    body = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.title
