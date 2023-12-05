"""Books app serializers"""
from rest_framework.serializers import ModelSerializer

from books.models import Book


class BookSerializer(ModelSerializer):
    """Book model serializer"""

    class Meta:
        model = Book
        fields = (
            "content",
            "created",
            "id",
            "title",
        )