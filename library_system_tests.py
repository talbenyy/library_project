import unittest
import valid_inputs
from Library import Library


class LibrarySystemTests(unittest.TestCase):
    def setUp(self):
        self.library = Library()

    # ----------- Unlogical Input -------------

    # String when int is expected
    def str_when_int_expected(self):
        pass

    # Negative numbers when positive are expected
    def neg_when_pos_expected(self):
        pass

    # Over 9 digits ID when expected up to 9 digits
    def over_9_digits_id(self):
        pass

    # Invalid Email
    def invalid_email(self):
        pass

    # ---------- Class Logic - Adding new instances ------------

    # Customer
    def test_add_new_customer(self):
        self.library.add_customer(388989827, "tal", "Tel Aviv", "tal9292@gmail.com", "2000-09-02")
        self.assertIn(self.library.find_customer_by_id(388989827), self.library.customers)

    # Book
    def test_add_new_book(self):
        self.library.add_book(777777777, "The Great Gatsby", "F. Scott Fitzgerald", 1925, 3)
        self.assertIn(self.library.find_book_by_id(777777777), self.library.books)

    # Loan
    def test_book_loan(self):
        self.library.add_customer(388989827, "tal", "Tel Aviv", "tal9292@gmail.com", "2000-09-02")
        self.library.add_book(777777777, "The Great Gatsby", "F. Scott Fitzgerald", 1925, 3)
        self.library.loan_book(388989827, 777777777)
        self.assertIn(self.library.find_loan_by_book_id(777777777), self.library.loans)

    # --------- Class Logic - Finding By ID ---------------

    # Book
    def test_find_book_by_id(self):
        self.library.add_book(777777777, "The Great Gatsby", "F. Scott Fitzgerald", 1925, 3)
        self.assertIn(self.library.find_book_by_id(777777777), self.library.books)

    # Customer
    def test_find_customer_by_id(self):
        self.library.add_customer(388989827, "tal", "Tel Aviv", "tal9292@gmail.com", "2000-09-02")
        self.assertIn(self.library.find_customer_by_id(388989827), self.library.customers)

    # --------- Class Logic - Removing instances ------------

    # Customer
    def test_remove_customer(self):
        self.library.add_customer(388989827, "tal", "Tel Aviv", "tal9292@gmail.com", "2000-09-02")
        self.library.remove_customer(388989827)
        self.assertIsNone(self.library.find_customer_by_id(388989827), self.library.customers)

    # Book
    def test_remove_book(self):
        self.library.add_book(777777777, "The Great Gatsby", "F. Scott Fitzgerald", 1925, 3)
        self.library.remove_book(777777777)
        self.assertIsNone(self.library.find_book_by_id(777777777), self.library.books)

    # Loan
    def test_return_book(self):
        self.library.add_customer(388989827, "tal", "Tel Aviv", "tal9292@gmail.com", "2000-09-02")
        self.library.add_book(777777777, "The Great Gatsby", "F. Scott Fitzgerald", 1925, 3)
        self.library.loan_book(388989827, 777777777)
        self.library.return_book(388989827, 777777777)
        self.assertIsNone(self.library.find_loan(388989827, 777777777), self.library.loans)


if __name__ == '__main__':
    unittest.main()
