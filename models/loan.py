from datetime import datetime


class Loan:

    def __init__(self, user_id: int, book_id: int):
        self.id: int = -1
        self.user_id = user_id
        self.book_id = book_id
        self.loan_date = datetime.now()
        self.returned = False

    def mark_as_returned(self):
        self.returned = True

    def __str__(self):
        status = "Returned" if self.returned else "On Loan"
        return f"Book ID: {self.book_id}, User ID: {self.user_id}, Status: {status}"
