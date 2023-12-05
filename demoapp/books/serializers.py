"""Books app serializers"""
from rest_framework.serializers import ModelSerializer

from books.models import Book, Author


class AuthorSerializer(ModelSerializer):
    """Author model serializer"""

    class Meta:
        """meta class"""
        model = Author
        fields = (
            "name",
        )


class BookSerializer(ModelSerializer):
    """Book model serializer"""

    class Meta:
        model = Book
        fields = (
            # "author",
            "content",
            "created",
            "id",
            "title",
        )