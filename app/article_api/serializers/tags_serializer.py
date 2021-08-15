from rest_framework.serializers import Serializer, CharField, ValidationError
from datetime import datetime


class GetTagSerializer(Serializer):

    tag = CharField(required=True)
    date = CharField(required=True)

    def validate_date(self, date):
        try:
            formatted_date = datetime.strptime(date, "%Y%m%d")
            return formatted_date
        except ValueError:
            raise ValidationError("Invalid date provided.")
