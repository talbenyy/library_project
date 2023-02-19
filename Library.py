# --------- Save/Restore ----------

import pickle

# -------- Other Classes -----------

from datetime import datetime
from Loan import Loan
from Customer import Customer
from Book import Book

# ---------- Exceptions For The Class -----------

from Library_Exceptions.BookAlreadyLoaned import BookAlreadyLoaned
from Library_Exceptions.IdAlreadyExists import IdAlreadyExists
from Library_Exceptions.InvalidId import InvalidId


# --------------- C L A S S -------------------

class Library:
    def __init__(self):
        self.books = []  # Books DB Of The Library
        self.customers = []  # Customers DB Of The Library
        self.loans = []  # Loans DB Of The Library

    # --------- Extra Functions - Utilities --------------

    # Function returns a Customer by a given ID parameter.
    # If it doesn't exist - function returns None.
    def find_customer_by_id(self, customer_id: int) -> Customer or None:
        for customer in self.customers:
            if customer.get_id() == customer_id:
                return customer
        return None

    # Function returns a Book by a given ID number.
    # If it doesn't exist - function returns None.
    def find_book_by_id(self, book_id: int) -> Book or None:
        for book in self.books:
            if book.get_book_id() == book_id:
                return book
        return None

    # Function returns a Loan by 2 parameters given - customer ID, book ID.
    # If it doesn't exist - function returns None.
    def find_loan(self, customer_id: int, book_id: int) -> Loan or None:
        for loan in self.loans:
            if loan.get_customer_id() == customer_id and loan.get_book_id() == book_id:
                return loan
        return None

    # Function returns all Loans by a customer ID parameter given.
    # If it doesn't exist - function returns an empty List.
    def find_loans_by_customer_id(self, customer_id: int) -> list:
        loans = []
        for loan in self.loans:
            if loan.customer_id == customer_id:
                loans.append(loan)
        return loans

    # Function returns a Loan matches a book given.
    # If it doesn't exist - function returns None.
    def find_loan_by_book_id(self, book_id) -> Loan or None:
        for loan in self.loans:
            if loan.book_id == book_id:
                return loan
        return None

    # ------------ Functions Of Project --------------

    # Function adds a Customer to the Customers array by relevant parameters given.
    def add_customer(self, customer_id: int, name: str, address: str, email: str, birthday: str) -> str:
        if self.find_customer_by_id(customer_id):
            raise IdAlreadyExists(" * Error - Customer ID already exists. * \n")
        else:
            customer = Customer(customer_id, name, address, email, birthday)
            self.customers.append(customer)
            return "\n * Customer Added: " + name + " * \n"

    # Function adds a Book to the Books array by relevant parameters given.
    def add_book(self, book_id: int, name: str, author: str, year_published: int, book_type: int) -> str:
        if self.find_book_by_id(book_id):
            raise IdAlreadyExists("\n * Error - Book ID already exists. * \n")
        else:
            book = Book(book_id, name, author, year_published, book_type)
            self.books.append(book)
            return "\n * Book Added: " + name + " * \n"

    # Function adds a Loan to the Loans array by relevant parameters given.
    def loan_book(self, customer_id: int, book_id: int) -> str:
        customer = self.find_customer_by_id(customer_id)
        book = self.find_book_by_id(book_id)

        if customer is None or book is None:
            raise InvalidId("\n * Error - Invalid customer ID or book ID. * \n")

        if self.find_loan(customer_id, book_id):
            raise BookAlreadyLoaned("\n * Error - Book already loaned. * \n")

        loan = Loan(customer_id, book_id, book.get_book_type())
        self.loans.append(loan)
        return "\n * Book Loaned: " + book.get_name() + " * \n"

    # Function removes a Loan from the Loans array by relevant parameters given.
    def return_book(self, customer_id: int, book_id: int) -> str:
        loan = self.find_loan(customer_id, book_id)

        if loan is None:
            raise InvalidId("\n * Error - Invalid customer ID or book ID. * \n")

        self.loans.remove(loan)
        return "\n * Book returned by customer: " + str(loan.get_customer_id()) + " * \n"

    # Function prints all Books that exist at the Books array.
    def display_all_books(self) -> list or str:
        if not self.books:
            return "\n * No books in library. * \n"
        else:
            return self.books

    # Function prints all Customers that exist at the Customers array.
    def display_all_customers(self) -> list or str:
        if not self.customers:
            return "\n * No customers in library. * \n"
        else:
            return self.customers

    # Function prints all Loans that exist at the Loans array.
    def display_all_loans(self) -> list or str:
        if not self.loans:
            return "\n * No books loaned. * \n"
        return self.loans

    # Function prints all Expired Loans that exist at the Loans array.
    def display_late_loans(self) -> list or str:
        if not self.loans:
            return "\n * No books loaned. * \n"
        late_loans = []
        for loan in self.loans:
            if loan.get_return_date() < datetime.now():
                late_loans.append(loan)
        if len(late_loans) == 0:
            return "\n * No late loans * \n"
        return late_loans

    # Function returns all Loans for a specific Customer by a given parameter ID number.
    def display_customer_loans(self, customer_id: int) -> list or str:
        loans = self.find_loans_by_customer_id(customer_id)
        if not loans:
            return "\n * No loans found for customer ID: " + str(customer_id) + " * \n"
        return loans

    # Function returns a Book from Books array by a given name parameter.
    def find_books_by_name(self, name: str) -> list or str:
        result = [book for book in self.books if name.lower() in book.get_name().lower()]
        if not result:
            return "\n * No books found by name: " + name + " * \n"
        return result

    # Function returns a Book from Books array by a given name parameter
    def find_books_by_author(self, author: str) -> list or str:
        result = [book for book in self.books if author.lower() in book.get_author().lower()]
        if not result:
            return "\n * No books found by author: " + author + " * \n"
        return result

    # Function returns a Customer from Customers array by a given name parameter
    def find_customer_by_name(self, name: str) -> Customer or str:
        result = [customer for customer in self.customers if name.lower() in customer.get_name().lower()]
        if not result:
            return "\n * No customers found by name: " + name + " * \n"
        return result

    # Function removes a Book from the Books array by a given ID parameter
    def remove_book(self, book_id: int) -> str:
        book = self.find_book_by_id(book_id)

        if book is None:
            raise InvalidId("\n * Error - Invalid book ID. * \n")

        if self.find_loan_by_book_id(book_id) is not None:
            raise BookAlreadyLoaned("\n * Error - Book Currently loaned. * \n")

        self.books.remove(book)

        return "\n * Book removed from library: " + book.get_name() + " * \n"

    # Function removes a Customer from the Customers array by a given ID parameter
    def remove_customer(self, customer_id: int) -> str:
        customer = self.find_customer_by_id(customer_id)

        if customer is None:
            raise InvalidId("\n * Error - Invalid customer ID. * \n")

        if self.find_loans_by_customer_id(customer_id):
            raise BookAlreadyLoaned("\n * Error - Customer Has A Currently loaned Book. * \n")

        self.customers.remove(customer)

        return "\n * Customer removed from list: " + str(customer_id) + " * \n"

    # ------------- Save/Restore Data Functions ------------------

    # Function restores the last instance file of Library. If not existed, a new one will be created.
    @staticmethod
    def load_library(filename):
        try:
            with open(filename, 'rb') as file:
                library = pickle.load(file)
                print(f"\n * Successfully loaded library from {filename}. * \n")
                return library
        except FileNotFoundError:
            print(f"\n * Error: file {filename} not found. * \n")
        except Exception as e:
            print(f"\n * Error: {str(e)} * \n")

    # Function saves the current instance of Library to a Pickle file.
    # This method happens after every user action at the menu so data won't get lost
    @staticmethod
    def save_library(filename, library):
        try:
            with open(filename, 'wb') as file:
                pickle.dump(library, file)
        except Exception as e:
            print(f"\n * Error: {str(e)} * \n")
