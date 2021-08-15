"""
App config for article_api project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

from django.apps import AppConfig


class ArticleAPIConfig(AppConfig):
    name = "article_api"
