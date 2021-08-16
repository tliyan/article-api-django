from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime

from article_api.models import Article
from article_api.serializers.tags_serializer import GetTagSerializer


class Tags(APIView):
    def get(self, request, tag=None, date=None):

        # Serialize data
        serializer = GetTagSerializer(data={"tag": tag, "date": date})
        serializer.is_valid(raise_exception=True)

        # At this point, the date should be valid as we validated this in the serializer
        # Reference: https://stackoverflow.com/questions/9750330/how-to-convert-integer-into-date-object-python
        formatted_date = datetime.strptime(date, "%Y%m%d")

        article_query = Article.objects.filter(
            date=formatted_date, tag__tag=tag
        ).order_by("id")

        if article_query:
            data = {
                "tag": tag,
                "count": article_query.count(),
                # Only last 10 articles will be included
                "articles": [str(article.id) for article in article_query][-10:],
                # Iterates through all of the tags across all of the articles and grabs
                # the tag name. We cast it as a set to ensure uniqueness and use the sorted
                # function to guarantee the output will always be in the same order (as sets
                # are unordered)
                "related_tags": sorted(
                    {
                        article_tag.tag
                        for article in article_query
                        for article_tag in article.tag_set.all().order_by("tag")
                        # related tags should not include requested tag
                        if article_tag.tag != tag
                    }
                ),
            }
            return Response(data=data, status=status.HTTP_200_OK)
        else:
            return Response(data={}, status=status.HTTP_404_NOT_FOUND)
