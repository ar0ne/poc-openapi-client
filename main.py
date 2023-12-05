"""
Demo script that uses generated api client.
"""
import uuid

from demo_api_client import Client
from demo_api_client.api.api import (
    api_v1_books_list as get_all_books,
    api_v1_books_retrieve as get_book_by_id,
    api_v1_books_create as create_book,
    api_v1_books_encrypt_create as encrypt_book_content,
    api_v1_books_decrypt_create as decrypt_book_content,
)
from demo_api_client.types import Response
from demo_api_client.models import Book, BookRequest, PaginatedBookList, DecryptDataInlineRequest


def main():
    client = Client(base_url="http://localhost:8000")

    books: PaginatedBookList | None
    with client as client:
        books = get_all_books.sync(client=client)

        book = books.results[0]

        book_details: Response[Book] = get_book_by_id.sync_detailed(book.id, client=client)

        print(book_details)

        # create new book
        new_book_request = BookRequest(content=book_details.parsed.content, title=str(uuid.uuid4()))
        new_book = create_book.sync(client=client, json_body=new_book_request, form_data=new_book_request, multipart_data=new_book_request)

        print(new_book.id)

        books = get_all_books.sync(client=client)
        print(books.count)

        encrypted_book_content = encrypt_book_content.sync(new_book.id, client=client)
        print(encrypted_book_content.data)

        data = DecryptDataInlineRequest(data=encrypted_book_content.data)
        decrypted_content = decrypt_book_content.sync(client=client, json_body=data, form_data=data, multipart_data=data)

        print(decrypted_content.result)


if __name__ == "__main__":
    main()

