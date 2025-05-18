from typing import Optional

from models.book import Book
from repositories.book_repositorie import IBookRepository


class BookService:

    def __init__(self, book_repositorie: IBookRepository):
        self.__book_repositorie = book_repositorie
    
    def add_book(self, book: Book):
        if self.__book_repositorie.find_by_id(book.id):
            raise ValueError(f"Book with ID: {book.id} already exists.")
        
        self.__book_repositorie.add(book)

    def get_book_by_id(self, book_id: int) -> Optional[Book]:
        return self.__book_repositorie.find_by_id(book_id)
    
    def list_books(self):
        return self.__book_repositorie.list_all()
    