from rest_framework.serializers import Serializer, CharField, DateField, ListField


class CreateArticleSerializer(Serializer):

    title = CharField(required=True)
    date = DateField(required=True)
    body = CharField(required=True)
    tags = ListField(child=CharField(), allow_empty=True)
