"""
Books views
"""
import base64

from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, inline_serializer
from rest_framework import viewsets, status, serializers
from rest_framework.decorators import action
from rest_framework.response import Response

from books.models import Author, Book
from books.serializers import AuthorSerializer, BookSerializer


def encrypt(data: str) -> str:
    """Dummy encrypt function"""
    content_bytes = data.encode("utf-8")
    return base64.b64encode(content_bytes).decode("utf-8")


def decrypt(data: str) -> str:
    """Dummy decrypt function"""
    return base64.b64decode(data.encode("utf-8")).decode("utf-8")


class AuthorViewSet(viewsets.ModelViewSet):
    """Author view set"""

    queryset = Author.objects.all()
    permission_classes = ()
    serializer_class = AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    """Books view set"""

    queryset = Book.objects.all()
    permission_classes = ()
    serializer_class = BookSerializer

    @extend_schema(
        request=None,
        responses={
            201: inline_serializer(
                name="EncryptDataInlineSerializer",
                fields={"data": serializers.CharField()}
            )
        },
    )
    @action(detail=True, methods=["post"])
    def encrypt(self, request, pk=None) -> Response:
        """Encrypt book content"""
        book = self.get_object()
        return Response(data={"data": encrypt(book.content)}, status=status.HTTP_201_CREATED)

    @extend_schema(
        request=inline_serializer(
            name="DecryptDataInlineSerializer",
            fields={"data": serializers.CharField()}
        ),
        responses={
            201: inline_serializer(
                name="DecryptOutputInlineSerializer",
                fields={"result": serializers.CharField()}
            )
        }
    )
    @action(detail=False, methods=["post"])
    def decrypt(self, request, pk=None) -> Response:
        """Decrypt book content"""
        data = request.data.get("data")
        return Response(
            data={"result": decrypt(data)},
            status=status.HTTP_201_CREATED
        )
