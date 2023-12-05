"""
Books views
"""

from rest_framework import viewsets

from books.models import Book
from books.serializers import BookSerializer


class BooksViewSet(viewsets.ModelViewSet):
    """Books view set"""

    queryset = Book.objects.all()
    permission_classes = ()
    serializer_class = BookSerializer

