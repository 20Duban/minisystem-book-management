from abc import ABC, abstractmethod
from models.loan import Loan


class ILoanRepository(ABC):

    @abstractmethod
    def add(self, loan: Loan):
        pass
    
    @abstractmethod
    def find_active_loan_by_book(self, book_id: int) -> Loan:
        pass

    @abstractmethod
    def list_all(self) -> list[Loan]:
        pass
