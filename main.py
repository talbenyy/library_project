import valid_inputs

from Library import Library
from Library_Exceptions.BookAlreadyLoaned import BookAlreadyLoaned
from Library_Exceptions.EmptyError import EmptyError
from Library_Exceptions.IdAlreadyExists import IdAlreadyExists
from Library_Exceptions.InvalidId import InvalidId


def main():
    library = Library.load_library('lib_data.pickle')
    if library is None:
        library = Library()
        print(" * new library file loaded * ")

    while True:
        print("\n ----------------------------------------- \n")
        print(" Library Menu: \n")
        print("1. Add a new customer")
        print("2. Add a new book")
        print("3. Loan a book")
        print("4. Return a book")
        print("5. Display all books")
        print("6. Display all customers")
        print("7. Display all loans")
        print("8. display all late loans")
        print("9. Display all loans for specific customer")
        print("10. Find books by name")
        print("11. Find books by author")
        print("12. Find customer by name")
        print("13. Remove a book from library")
        print("14. Remove a customer from library")
        print("15. Quit")
        print("\n ----------------------------------------- \n")
        choice = valid_inputs.choice_input()

        try:
            if choice == 1:
                customer_id = valid_inputs.customer_id_input()
                name = valid_inputs.customer_name_input()
                address = valid_inputs.customer_address_input()
                email = valid_inputs.customer_email_input()
                birthday = valid_inputs.customer_birthday_input()
                print(library.add_customer(customer_id, name, address, email, birthday))

            if choice == 2:
                book_id = valid_inputs.book_id_input()
                name = valid_inputs.book_name_input()
                author = valid_inputs.book_author_input()
                year = valid_inputs.book_year_input()
                book_type = valid_inputs.book_type_input()
                print(library.add_book(book_id, name, author, year, book_type))

            elif choice == 3:
                customer_id = valid_inputs.customer_id_input()
                book_id = valid_inputs.book_id_input()
                print(library.loan_book(customer_id, book_id))

            elif choice == 4:
                book_id = valid_inputs.book_id_input()
                customer_id = valid_inputs.customer_id_input()
                print(library.return_book(customer_id, book_id))

            elif choice == 5:
                print("\n Here's What I Found For You: \n ")
                books = library.display_all_books()
                if books is list:
                    for book in books:
                        print(book)
                else:
                    print(books)

            elif choice == 6:
                print("\n Here's What I Found For You: \n ")
                customers = library.display_all_customers()
                if customers is list:
                    for customer in customers:
                        print(customer)
                else:
                    print(customers)

            elif choice == 7:
                print("\n Here's What I Found For You: \n ")
                loans = library.display_all_loans()
                if loans is list:
                    for loan in loans:
                        print(loan)
                else:
                    print(loans)

            elif choice == 8:
                print("\n Here's What I Found For You: \n ")
                loans = library.display_late_loans()
                if loans is list:
                    for loan in loans:
                        print(loan)
                else:
                    print(loans)

            elif choice == 9:
                print("\n Here's What I Found For You: \n ")
                customer_id = valid_inputs.customer_id_input()
                loans = library.display_customer_loans(customer_id)
                if loans is list:
                    for loan in loans:
                        print(loan)
                else:
                    print(loans)

            elif choice == 10:
                name = valid_inputs.book_name_input()
                books = library.find_books_by_name(name)
                print("\n Here's What I Found For You: \n ")
                if books is list:
                    for book in books:
                        print(book)
                else:
                    print(books)

            elif choice == 11:
                author = valid_inputs.book_author_input()
                books = library.find_books_by_author(author)
                print("\n Here's What I Found For You: \n ")
                if books is list:
                    for book in books:
                        print(book)
                else:
                    print(books)

            elif choice == 12:
                name = valid_inputs.customer_name_input()
                print("\n Here's What I Found For You: \n ")
                print(library.find_customer_by_name(name))

            elif choice == 13:
                book_id = valid_inputs.book_id_input()
                print(library.remove_book(book_id))

            elif choice == 14:
                customer_id = valid_inputs.customer_id_input()
                print(library.remove_customer(customer_id))

            elif choice == 15:
                print("\n * Thank You For Using Library System * \n")
                exit(0)

        except ValueError as e:
            print("\n * Error - Please Enter A Valid Value * \n")
        except BookAlreadyLoaned as e:
            print("\n * Error - Book Chosen Is Already Loaned * \n")
        except EmptyError as e:
            print("\n * Error - This List Is Empty * \n")
        except IdAlreadyExists as e:
            print("\n * Error - Id Given Already Exists * \n")
        except InvalidId as e:
            print("\n * Error - Please Insert A Valid ID Number * \n")
        except Exception as e:
            print("\n * Error - An Error Occurred. Here Are some Details About It >> * \n ", e)
        finally:
            library.save_library('lib_data.pickle', library)


if __name__ == '__main__':
    main()


