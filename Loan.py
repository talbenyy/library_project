from datetime import datetime, timedelta


class Loan:
    def __init__(self, customer_id: int, book_id: int, book_type: int):
        self.customer_id = customer_id
        self.book_id = book_id
        self.loan_date = datetime.today()  # Loan time is current time :)

        days = None
        if book_type == '1':
            days = 10
        if book_type == '2':
            days = 5
        if book_type == '3':
            days = 2

        self.return_date = self.loan_date + timedelta(days=days)  # Return date will be according to book type.

    def get_customer_id(self) -> int:
        return self.customer_id

    def set_customer_id(self, customer_id: int):
        self.customer_id = customer_id

    def get_book_id(self) -> int:
        return self.book_id

    def set_book_id(self, book_id: int):
        self.book_id = book_id

    def get_loan_date(self):
        return self.loan_date

    def set_loan_date(self, loan_date):
        self.loan_date = loan_date

    def get_return_date(self):
        return self.return_date

    def __str__(self) -> str:
        return f"{self.customer_id} - {self.book_id} loan date: {self.loan_date}, return date: {self.return_date})"

    def __repr__(self) -> str:
        return f"{self.customer_id} - {self.book_id} loan date: {self.loan_date}, return date: {self.return_date})"
