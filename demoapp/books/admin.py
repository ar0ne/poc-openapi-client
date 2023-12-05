"""
Admin interface for Books app
"""
from django.contrib import admin

from books.models import Author, Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    """Author admin page"""
    list_display = (
        "id",
        "name",
    )


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """Book admin page"""
    list_display = (
        "id",
        "title",
    )
    search_fields = (
        "author__id",
        "id",
    )