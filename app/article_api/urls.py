"""
Article API URL Configuration

"""
from django.urls import path

from article_api.views.articles import Articles
from article_api.views.tags import Tags


urlpatterns = [
    path("articles", Articles.as_view()),
    path("articles/<int:id>", Articles.as_view()),
    path("tags/<str:tag>/<str:date>", Tags.as_view()),
]
