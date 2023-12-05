import uuid

from django.db import models
from model_utils.models import SoftDeletableModel, TimeStampedModel


class BaseModel(TimeStampedModel, SoftDeletableModel):
    """Base model"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        """meta class"""
        abstract = True


class Author(BaseModel):
    """Author model"""
    name = models.CharField(max_length=50)
    books = models.ManyToManyField("Book", related_name="authors")


class Book(BaseModel):
    """Book model"""
    title = models.CharField(max_length=50)
    content = models.TextField()
