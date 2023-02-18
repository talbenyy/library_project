class Loan:
    def __init__(self, customer_id, book_id, loan_date, return_date):
        self.customer_id = customer_id
        self.book_id = book_id
        self.loan_date = loan_date
        self.return_date = return_date

    def get_customer_id(self):
        return self.customer_id

    def set_customer_id(self, customer_id):
        self.customer_id = customer_id

    def get_book_id(self):
        return self.book_id

    def set_book_id(self, book_id):
        self.book_id = book_id

    def get_loan_date(self):
        return self.loan_date

    def set_loan_date(self, loan_date):
        self.loan_date = loan_date

    def get_return_date(self):
        return self.return_date

    def set_return_date(self, return_date):
        self.return_date = return_date
