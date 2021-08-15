import pytest


@pytest.mark.django_db()
def test_get_tags_invalid_tag_no_result(client):
    expected_response = {}

    response = client.get(
        "/tags/tag-that-doesnt-exist/20161209", content_type="application/json"
    )

    # Verify Response
    assert response.status_code == 404
    assert response.json() == expected_response


@pytest.mark.django_db()
def test_get_tags_invalid_date_no_result(client):
    expected_response = {"date": ["Invalid date provided."]}

    response = client.get("/tags/science/20161309", content_type="application/json")

    # Verify Response
    assert response.status_code == 400
    assert response.json() == expected_response


@pytest.mark.django_db(reset_sequences=True)
def test_get_tags_single_article_unique_tag_result(client, create_articles):
    expected_response = {
        "tag": "sports",
        "count": 1,
        "articles": ["5"],
        "related_tags": ["business", "finance"],
    }

    response = client.get("/tags/sports/20161209", content_type="application/json")

    # Verify Response
    assert response.status_code == 200
    assert response.json() == expected_response


@pytest.mark.django_db(reset_sequences=True)
def test_get_tags_single_article_common_tag_result(client, create_articles):
    expected_response = {
        "tag": "science",
        "count": 1,
        "articles": ["4"],
        "related_tags": ["business", "finance", "health"],
    }

    response = client.get("/tags/science/20151209", content_type="application/json")

    # Verify Response
    assert response.status_code == 200
    assert response.json() == expected_response


@pytest.mark.django_db(reset_sequences=True)
def test_get_tags_multiple_article_result(client, create_articles):
    # Related tags should contain tags from both article #2 and #3
    expected_response = {
        "tag": "science",
        "count": 2,
        "articles": ["2", "3"],
        "related_tags": ["finance", "fitness", "health"],
    }

    response = client.get("/tags/science/20161209", content_type="application/json")

    # Verify Response
    assert response.status_code == 200
    assert response.json() == expected_response


@pytest.mark.django_db(reset_sequences=True)
def test_get_tags_ten_plus_results(client, create_articles):
    # Articles should be capped to the last 10 results, even though there are more
    # than 10 articles
    expected_response = {
        "tag": "finance",
        "count": 12,
        "articles": ["5", "6", "7", "8", "9", "10", "11", "12", "13", "14"],
        "related_tags": [
            "business",
            "fitness",
            "food",
            "health",
            "science",
            "sports",
            "tech",
        ],
    }

    response = client.get("/tags/finance/20161209", content_type="application/json")

    # Verify Response
    assert response.status_code == 200
    assert response.json() == expected_response
