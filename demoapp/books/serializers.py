"""Books app serializers"""
from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import ModelSerializer

from books.models import Book, Author


class AuthorSerializer(ModelSerializer):
    """Author model serializer"""

    class Meta:
        """meta class"""
        model = Author
        fields = (
            "name",
            "id",
        )


class BookSerializer(ModelSerializer):
    """Book model serializer"""

    authors = AuthorSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Book
        fields = (
            "authors",
            "content",
            "created",
            "id",
            "title",
        )