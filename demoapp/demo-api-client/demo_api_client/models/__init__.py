""" Contains all the data models used in inputs/outputs """

from .author import Author
from .author_request import AuthorRequest
from .book import Book
from .book_request import BookRequest
from .decrypt_data_inline_request import DecryptDataInlineRequest
from .paginated_book_list import PaginatedBookList
from .patched_book_request import PatchedBookRequest

__all__ = (
    "Author",
    "AuthorRequest",
    "Book",
    "BookRequest",
    "DecryptDataInlineRequest",
    "PaginatedBookList",
    "PatchedBookRequest",
)
