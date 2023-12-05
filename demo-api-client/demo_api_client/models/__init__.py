""" Contains all the data models used in inputs/outputs """

from .book import Book
from .book_request import BookRequest
from .paginated_book_list import PaginatedBookList
from .patched_book_request import PatchedBookRequest

__all__ = (
    "Book",
    "BookRequest",
    "PaginatedBookList",
    "PatchedBookRequest",
)
