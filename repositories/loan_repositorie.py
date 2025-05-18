from typing import Optional
from models.loan import Loan
from abc import ABC, abstractmethod


class ILoanRepository(ABC):

    @abstractmethod
    def add(self, loan: Loan):
        pass
    
    @abstractmethod
    def find_by_id(self, loan_id: int) -> Optional[Loan]:
        pass

    @abstractmethod
    def find_active_loan_by_book(self, book_id: int) -> Loan:
        pass

    @abstractmethod
    def list_all(self) -> list[Loan]:
        pass
