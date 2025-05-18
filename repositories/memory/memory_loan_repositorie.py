from typing import List, Optional

from models.loan import Loan
from repositories.loan_repositorie import ILoanRepository


class MemoryLoanRepository(ILoanRepository):

    def __init__(self):
        self.loans: List[Loan] = []

    def add(self, loan: Loan):
        self.loans.append(loan)

    def find_active_loan_by_book(self, book_id: int) -> Optional[Loan]:
        loan_found = None

        for loan in self.loans:
            if loan.book_id == book_id and not loan.returned:
                loan_found = loan
                break

        return loan_found

    def list_all(self) -> List[Loan]:
        return self.loans.copy()
