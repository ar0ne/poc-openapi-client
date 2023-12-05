import uuid
from typing import List

from django.db import models
from model_utils.models import SoftDeletableModel, TimeStampedModel


class BaseModel(TimeStampedModel, SoftDeletableModel):
    """Base model"""

    id: uuid.UUID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        """meta class"""
        abstract = True


class Author(BaseModel):
    """Author model"""
    name: str = models.CharField(max_length=50)
    books: List["Author"] = models.ManyToManyField("Book", blank=True, related_name="authors")

    def __str__(self) -> str:
        """To string"""
        return self.name


class Book(BaseModel):
    """Book model"""
    title: str = models.CharField(max_length=50)
    content: str = models.TextField()

    def __str__(self) -> str:
        """To string"""
        return self.title
