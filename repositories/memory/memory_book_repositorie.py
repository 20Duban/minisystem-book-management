from typing import Optional

from repositories.book_repositorie import Book
from repositories.book_repositorie import IBookRepository


class MemoryBookRepositorie(IBookRepository):
    
    def __init__(self):
        self.__books: list[Book] = []

    def add(self, book: Book):
        self.__books.append(book)
    
    def find_by_id(self, book_id: int) -> Optional[Book]:
        book_found = None

        for book in self.__books:
            if book_id == book.id:
                book_found = book
                break

        return book_found

    def list_all(self) -> list[Book]:
        return self.__books.copy()
