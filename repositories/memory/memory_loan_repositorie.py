from typing import List, Optional

from models.loan import Loan
from repositories.loan_repositorie import ILoanRepository


class MemoryLoanRepository(ILoanRepository):

    def __init__(self):
        self.loans: List[Loan] = []
        self.__current_id = 1

    def add(self, loan: Loan):
        loan.id = self.__current_id
        self.loans.append(loan)
        self.__current_id += 1

    def find_by_id(self, loan_id: int) -> Optional[Loan]:
        loan_found = None
        for loan in self.loans:
            if loan.id == loan_id:
                loan_found = loan
                break

        return loan_found

    def find_active_loan_by_book(self, book_id: int) -> Optional[Loan]:
        loan_found = None

        for loan in self.loans:
            if loan.book_id == book_id and not loan.returned:
                loan_found = loan
                break

        return loan_found


    def delete_loan(self, loan_id: int):
        for index, loan in enumerate(self.loans):
            if loan.id == loan_id:
                del self.loans[index]
                break

    def list_all(self) -> List[Loan]:
        return self.loans.copy()
