import pytest

from article_api.models import Article


@pytest.mark.django_db()
def test_create_articles_no_data(client):

    expected_response = {
        "title": ["This field is required."],
        "date": ["This field is required."],
        "body": ["This field is required."],
        "tags": ["This field is required."],
    }

    # No data in request
    request = {}

    response = client.post("/articles", request, content_type="application/json")

    # Verify Response
    assert response.status_code == 400
    assert response.json() == expected_response


@pytest.mark.django_db()
def test_create_articles_missing_data(client):

    expected_response = {
        "date": ["This field is required."],
        "tags": ["This field is required."],
    }

    # Request missing date attribute
    request = {
        "title": "Test Article Missing Data",
        "body": "Test to confirm whether an article with missing data throws a Validation error",
    }

    response = client.post("/articles", request, content_type="application/json")

    # Verify Response
    assert response.status_code == 400
    assert response.json() == expected_response


@pytest.mark.django_db()
def test_create_articles_invalid_data(client):

    expected_response = {
        "date": [
            "Date has wrong format. Use one of these formats instead: YYYY-MM-DD."
        ],
    }

    # Request missing date attribute
    request = {
        "title": "Test Article Missing Data",
        "body": "Test to confirm whether an article with invalid data throws a Validation error",
        "date": "Not-a-valid-date-value",
        "tags": [],
    }

    response = client.post("/articles", request, content_type="application/json")

    # Verify Response
    assert response.status_code == 400
    assert response.json() == expected_response


@pytest.mark.django_db(reset_sequences=True)
def test_create_articles_single_success(client):

    expected_response = {}

    title = "Test Articles Single Success"
    date = "2016-09-22"
    body = "Test to confirm whether an article is successfully created and stored in the database"
    tags = ["sport", "finance"]

    request = {
        "title": title,
        "date": date,
        "body": body,
        "tags": tags,
    }

    response = client.post("/articles", request, content_type="application/json")

    # Verify Response
    assert response.status_code == 201
    assert response.json() == expected_response

    # Verify Single Object Creation in DB
    articles = Article.objects.all().order_by("id")
    assert articles.count() == 1

    # Verify Article Attributes
    article = articles.get()
    assert article.id == 1
    assert article.title == title
    assert article.body == body
    assert [article_tag.tag for article_tag in article.tag_set.all()] == tags


@pytest.mark.django_db(reset_sequences=True)
def test_create_articles_multiple_success(client):

    expected_response = {}

    title_1 = "Test Articles Multiple Success #1"
    date_1 = "2016-09-22"
    body_1 = "Test to confirm whether an article is successfully created and stored in the database"
    tags_1 = ["sport", "finance"]

    request_1 = {
        "title": title_1,
        "date": date_1,
        "body": body_1,
        "tags": tags_1,
    }

    title_2 = "Test Articles Multiple Success #2"
    date_2 = "2016-10-22"
    body_2 = "Test to confirm whether an article is successfully created and stored in the database"
    tags_2 = ["business", "health", "science"]

    request_2 = {
        "title": title_2,
        "date": date_2,
        "body": body_2,
        "tags": tags_2,
    }

    response_1 = client.post("/articles", request_1, content_type="application/json")
    response_2 = client.post("/articles", request_2, content_type="application/json")

    # Verify Response
    assert response_1.status_code == 201
    assert response_1.json() == expected_response

    assert response_2.status_code == 201
    assert response_2.json() == expected_response

    # Verify Single Object Creation in DB
    articles = Article.objects.all().order_by("id")
    assert articles.count() == 2

    # Verify Article Attributes
    article_1 = articles.first()
    assert article_1.id == 1
    assert article_1.title == title_1
    assert article_1.body == body_1
    assert [article_tag.tag for article_tag in article_1.tag_set.all()] == tags_1

    article_2 = articles.last()
    assert article_2.id == 2
    assert article_2.title == title_2
    assert article_2.body == body_2
    assert [article_tag.tag for article_tag in article_2.tag_set.all()] == tags_2
