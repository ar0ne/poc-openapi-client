"""
Books views
"""

from rest_framework import viewsets

from books.models import Author, Book
from books.serializers import AuthorSerializer, BookSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    """Author view set"""

    queryset = Author.objects.all()
    permission_classes = ()
    serializer_class = AuthorSerializer


class BooksViewSet(viewsets.ModelViewSet):
    """Books view set"""

    queryset = Book.objects.all()
    permission_classes = ()
    serializer_class = BookSerializer

