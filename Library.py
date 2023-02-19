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

    # Function returns a Customer by a given ID parameter
    def find_customer_by_id(self, customer_id) -> Customer or None:
        for customer in self.customers:
            if customer.get_id() == customer_id:
                return customer
        return None

    # Function returns a Book by a given ID number
    def find_book_by_id(self, book_id) -> Book or None:
        for book in self.books:
            if book.get_book_id() == book_id:
                return book
        return None

    # Function returns a Loan by 2 parameters given - customer ID, book ID
    def find_loan(self, customer_id, book_id) -> Loan or None:
        for loan in self.loans:
            if loan.get_customer_id() == customer_id and loan.get_book_id() == book_id:
                return loan
        return None

    # Function returns a Loan by a customer ID parameter given
    def find_loans_by_customer_id(self, customer_id) -> list:
        loans = []
        for loan in self.loans:
            if loan.customer_id == customer_id:
                loans.append(loan)
        return loans

    # Function returns a Loan by a book ID parameter given
    def find_loans_by_book_id(self, book_id):
        loans = []
        for loan in self.loans:
            if loan.book_id == book_id:
                loans.append(loan)
        return loans

    # ------------ Functions Of Project --------------

    # Function adds a Customer to the Customers array by relevant parameters given
    def add_customer(self, customer_id, name, address, email, birthday):
        if self.find_customer_by_id(customer_id):
            raise IdAlreadyExists("Customer ID already exists.")
        else:
            customer = Customer(customer_id, name, address, email, birthday)
            self.customers.append(customer)

    # Function adds a Book to the Books array by relevant parameters given
    def add_book(self, book_id, name, author, year_published, book_type):
        if self.find_book_by_id(book_id):
            raise IdAlreadyExists("Book ID already exists")
        else:
            book = Book(book_id, name, author, year_published, book_type)
            self.books.append(book)

    # Function adds a Loan to the Loans array by relevant parameters given
    def loan_book(self, customer_id, book_id):
        customer = self.find_customer_by_id(customer_id)
        book = self.find_book_by_id(book_id)

        if customer is None or book is None:
            raise InvalidId("Invalid customer ID or book ID.")

        if self.find_loan(customer_id, book_id):
            raise BookAlreadyLoaned("Book already loaned.")

        loan = Loan(customer_id, book_id, book.get_book_type())
        self.loans.append(loan)

    # Function removes a Loan from the Loans array by relevant parameters given
    def return_book(self, customer_id, book_id):
        loan = self.find_loan(customer_id, book_id)

        if loan is None:
            raise InvalidId("Invalid customer ID or book ID.")

        self.loans.remove(loan)
        return "Book returned by customer: " + str(loan.get_customer_id())

    # Function prints all Books that exist at the Books array
    def display_all_books(self):
        if not self.books:
            return "No books in library."
        else:
            return self.books

    # Function prints all Customers that exist at the Customers array
    def display_all_customers(self):
        if not self.customers:
            return "No customers in library."
        else:
            return self.customers

    # Function prints all Loans that exist at the Loans array
    def display_all_loans(self):
        if not self.loans:
            return "No books loaned."
        return self.loans

    # Function prints all Expired Loans that exist at the Loans array
    def display_late_loans(self):
        if not self.loans:
            return "No books loaned."
        late_loans = []
        for loan in self.loans:
            if loan.get_return_date() < datetime.now():
                late_loans.append(loan)
        if len(late_loans) == 0:
            return "No late loans"
        return late_loans

    # Function prints all Loans for a specific Customer by a given parameter ID number
    def display_customer_loans(self, customer_id):
        loans = self.find_loans_by_customer_id(customer_id)
        if not loans:
            return "No loans found for customer ID: " + str(customer_id)
        return loans

    # Function returns a Book from Books array by a given name parameter
    def find_books_by_name(self, name):
        result = [book for book in self.books if name.lower() in book.get_name().lower()]
        if not result:
            return "No books found by name: " + name
        return result

    # Function returns a Book from Books array by a given name parameter
    def find_books_by_author(self, author):
        result = [book for book in self.books if author.lower() in book.get_author().lower()]
        if not result:
            return "No books found by author: " + author
        return result

    # Function returns a Customer from Customers array by a given name parameter
    def find_customer_by_name(self, name):
        result = [customer for customer in self.customers if name.lower() in customer.get_name().lower()]
        if not result:
            return "No customers found by name: " + name
        return result

    def remove_book(self, book_id):
        book = self.find_book_by_id(book_id)

        if book is None:
            raise InvalidId("Invalid book ID.")

        if self.find_loans_by_book_id(book_id):
            raise BookAlreadyLoaned("Book is currently loaned.")

        self.books.remove(book)

        return "Book removed from library: " + book.get_name()

    def remove_customer(self, customer_id):
        customer = self.find_customer_by_id(customer_id)

        if customer is None:
            raise InvalidId("Invalid customer ID.")

        if self.find_loans_by_customer_id(customer_id):
            raise BookAlreadyLoaned("Book is currently loaned.")

        self.customers.remove(customer)

        return "Customer removed from list: " + str(customer_id)

    # ------------- Save/Restore Data Functions ------------------

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
            print(f"Error: {str(e)}")

    @staticmethod
    def save_library(filename, library):
        try:
            with open(filename, 'wb') as file:
                pickle.dump(library, file)
        except Exception as e:
            print(f"Error: {str(e)}")
