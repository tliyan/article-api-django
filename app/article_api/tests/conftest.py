import pytest
import json
from django.test import Client
from django.conf import settings

from article_api.models import Article, Tag


@pytest.fixture(scope="session")
def client():
    c = Client()
    return c


@pytest.fixture()
@pytest.mark.django_db(reset_sequences=True)
def create_articles():

    test_data_path = (
        f"{settings.BASE_DIR}/app/article_api/tests/commons/test_data/article_data.json"
    )

    with open(test_data_path) as test_file:
        test_data = json.load(test_file)

        for test_case in test_data:
            test_article = Article.objects.create(
                title=test_case.get("title"),
                date=test_case.get("date"),
                body=test_case.get("body"),
            )

            for tag in test_case.get("tags", []):
                test_tag, _ = Tag.objects.get_or_create(tag=tag)
                test_tag.articles.add(test_article)
                test_tag.save()

        return test_data
