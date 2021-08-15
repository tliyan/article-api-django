from django.core.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from article_api.models import Article, Tag
from article_api.serializers.articles_serializer import CreateArticleSerializer


class Articles(APIView):
    def get(self, request, id=None):

        article_query = Article.objects.filter(id=id)

        # Only fetch data if the query for an article was successful
        if article_query:
            article = article_query.get()
            data = {
                "id": str(article.id),
                "title": article.title,
                "date": article.date,
                "body": article.body,
                "tags": [
                    article_tag.tag
                    for article_tag in article.tag_set.all().order_by("tag")
                ],
            }

            return Response(data=data, status=status.HTTP_200_OK)
        else:
            return Response(data={}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):

        # Serialize data
        serializer = CreateArticleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serialized_data = serializer.data

        article = Article.objects.create(
            title=serialized_data.get("title", ""),
            date=serialized_data.get("date", ""),
            body=serialized_data.get("body", ""),
        )

        for tag in serialized_data.get("tags", []):
            # We use get_or_create to ensure that if a tag already exists in the database,
            # we don't attempt to recreate it. (This will fail anyway due to the unique constraint we applied
            # on the Tag Model, but using get_or_create ensures we silently process this and will not throw
            # an unexpected error)
            tag, _ = Tag.objects.get_or_create(tag=tag)
            tag.articles.add(article)
            tag.save()

        return Response(data={}, status=status.HTTP_201_CREATED)
