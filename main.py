import json
import pickle
from datetime import datetime

from Library import Library
from Library_Exceptions.BookAlreadyLoaned import BookAlreadyLoaned
from Library_Exceptions.EmptyError import EmptyError
from Library_Exceptions.IdAlreadyExists import IdAlreadyExists
from Library_Exceptions.InvalidId import InvalidId


def main():
    library = Library.load_library('library2.pickle')
    if library is None:
        library = Library()
        print("new library file loaded")

    while True:
        print("-----------------------------------------")
        print("\n\nLibrary Menu:")
        # V
        print("1. Add a new customer")
        # V
        print("2. Add a new book")
        # V
        print("3. Loan a book")
        # V
        print("4. Return a book")
        # V
        print("5. Display all books")
        # V
        print("6. Display all customers")
        # V
        print("7. Display all loans")
        # X
        print("8. display all late loans")
        # V
        print("9. Display all loans for specific customer")
        # V
        print("10. Find books by name")
        # V
        print("11. Find books by author")
        # V
        print("12. Find customer by name")
        # V
        print("13. Remove a book from library")
        # V
        print("14. Remove a customer from library")
        # V
        print("15. Quit")
        print("-----------------------------------------")
        print()
        choice = input("Enter your choice (1-14) >> ")
        print()

        try:
            if choice == '1':
                customer_id = int(input("Enter customer id: "))
                name = input("Enter customer name: ")
                address = input("Enter customer address: ")
                email = input("Enter customer email: ")
                birthday = input("Enter customer birthday (YYYY-MM-DD): ")
                library.add_customer(customer_id, name, address, email, birthday)

            if choice == '2':
                book_id = int(input("Enter book id: "))
                name = input("Enter book name: ")
                author = input("Enter book author: ")
                year = input("Enter book year of publish: ")
                book_type = input("Enter a book type (for loan time)")
                library.add_book(book_id, name, author, year, book_type)

            elif choice == '3':
                customer_id = int(input("Enter customer id: "))
                book_id = int(input("Enter book id: "))
                library.loan_book(customer_id, book_id)

            elif choice == '4':
                book_id = int(input("Enter book id: "))
                customer_id = int(input("Enter customer id: "))
                library.return_book(customer_id, book_id)

            elif choice == '5':
                books = library.display_all_books()
                if books is list:
                    for book in books:
                        print(book)
                else:
                    print(books)

            elif choice == '6':
                customers = library.display_all_customers()
                if customers is list:
                    for customer in customers:
                        print(customer)
                else:
                    print(customers)

            elif choice == '7':
                loans = library.display_all_loans()
                if loans is list:
                    for loan in loans:
                        print(loan)
                else:
                    print(loans)

            elif choice == '8':
                loans = library.display_late_loans()
                if loans is list:
                    for loan in loans:
                        print(loan)
                else:
                    print(loans)

            elif choice == '9':
                customer_id = int(input("Enter customer id: "))
                loans = library.display_customer_loans(customer_id)
                if loans is list:
                    for loan in loans:
                        print(loan)
                else:
                    print(loans)

            elif choice == '10':
                name = input("Enter book name: ")
                books = library.find_books_by_name(name)
                if books is list:
                    for book in books:
                        print(book)
                else:
                    print(books)

            elif choice == '11':
                author = input("Enter author name: ")
                books = library.find_books_by_author(author)
                if books is list:
                    for book in books:
                        print(book)
                else:
                    print(books)

            elif choice == '12':
                name = input("Enter customer name: ")
                print(library.find_customer_by_name(name))

            elif choice == '13':
                book_id = int(input("Enter book id: "))
                library.remove_book(book_id)

            elif choice == '14':
                customer_id = int(input("Enter customer id:"))
                library.remove_customer(customer_id)

            elif choice == '15':
                print("Thank You For Using Library System")
                exit(0)

        except ValueError as e:
            print("Please Enter A Valid Value")
        except BookAlreadyLoaned as e:
            print("Book Chosen Is Already Loaned")
        except EmptyError as e:
            print("This List Is Empty")
        except IdAlreadyExists as e:
            print("Id Given Already Exists")
        except InvalidId as e:
            print("Please Insert A Valid ID Number")
        except Exception as e:
            print("An Error Occurred", e)
        finally:
            library.save_library('library2.pickle', library)


if __name__ == '__main__':
    main()


