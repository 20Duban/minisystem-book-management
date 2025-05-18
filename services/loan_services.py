
from models.loan import Loan
from models.user import User
from models.book import Book

from repositories.loan_repositorie import ILoanRepository
from repositories.user_repositorie import IUserRepository
from repositories.book_repositorie import IBookRepository


class LoanService:

    def __init__(
        self,
        loan_repositorie: ILoanRepository,
        user_repositorie: IUserRepository,
        book_repositorie: IBookRepository
    ):
        self.__loan_repositorie = loan_repositorie
        self.__user_repositorie = user_repositorie
        self.__book_repositorie = book_repositorie

    def borrow_book(self, book_id: int, user_id: int):
        book = self.__book_repositorie.find_by_id(book_id)
        user = self.__user_repositorie.find_by_id(user_id)

        if not book:
            raise ValueError(f"Book with ID: {book_id} not found.")
        if not user:
            raise ValueError(f"User with ID: {user_id} not found.")
        if not book.is_available:
            raise ValueError(f"Book with ID: {book_id} is not available.")

        book.is_available = False
        loan = Loan(user_id, book_id)

        self.__loan_repositorie.add(loan)

    def return_book(self, loan_id: int):
        loan = self.__loan_repositorie.find_by_id(loan_id)
        if not loan:
            raise ValueError(f"Loan with ID {loan_id} not found.")

        book = self.__book_repositorie.find_by_id(loan.book_id)
        if book:
            book.is_available = True


    def list_loans(self):
        return self.__loan_repositorie.list_all()