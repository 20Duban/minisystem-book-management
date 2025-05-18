from abc import ABC, abstractmethod
from models.book import Book


class IBookRepository(ABC):

    @abstractmethod
    def add(self, book: Book):
        pass
    
    @abstractmethod
    def find_by_id(self, book_id: int) -> Book:
        pass

    @abstractmethod
    def list_all(self) -> list[Book]:
        pass
