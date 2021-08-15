import pytest


@pytest.mark.django_db()
def test_get_articles_no_result(client):
    expected_response = {}

    response = client.get("/articles/11", content_type="application/json")

    # Verify Response
    assert response.status_code == 404
    assert response.json() == expected_response


@pytest.mark.django_db(reset_sequences=True)
def test_get_articles_result_no_tags(client, create_articles):

    expected_response = {
        "id": "1",
        "title": "Test Article #1",
        "date": "2016-12-09",
        "body": "Article created for testing purposes",
        "tags": [],
    }

    response = client.get("/articles/1", content_type="application/json")

    # Verify Response
    assert response.status_code == 200
    assert response.json() == expected_response


@pytest.mark.django_db(reset_sequences=True)
def test_get_articles_result_tags(client, create_articles):

    expected_response = {
        "id": "2",
        "title": "Test Article #2",
        "date": "2016-12-09",
        "body": "Article created for testing purposes",
        "tags": ["finance", "fitness", "health", "science"],
    }

    response = client.get("/articles/2", content_type="application/json")

    # Verify Response
    assert response.status_code == 200
    assert response.json() == expected_response
