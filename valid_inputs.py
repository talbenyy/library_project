import re


# ------------ input validations for Customer ---------------

def customer_id_input() -> int:
    while True:
        customer_id = input(" Please Enter Your ID Number >> ")
        pattern = r'^\d{9}$'
        match = re.search(pattern, str(customer_id))
        if match:
            return int(customer_id)
        print(" Please Try Again >> ")
        continue


def customer_name_input() -> str:
    while True:
        customer_name = input(" Please Enter Your Name >> ")
        pattern = r'^[a-zA-Z]+(([\'\,\.\- ][a-zA-Z ])?[a-zA-Z]*)*$'
        match = re.search(pattern, str(customer_name))
        if match:
            return customer_name
        print(" Please Try Again >> ")
        continue


def customer_address_input() -> str:
    while True:
        customer_address = input(" Please Enter Your Address >> ")
        pattern = r'^\d+\s+([a-zA-Z]+\s?)+[a-zA-Z]{2,}$'
        match = re.search(pattern, str(customer_address))
        if match:
            return customer_address
        print(" Please Try Again >> ")
        continue


def customer_email_input() -> str:
    while True:
        customer_email = input(" Please Enter Your Email Address >> ")
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        match = re.search(pattern, str(customer_email))
        if match:
            return customer_email
        print(" Please Try Again >> ")
        continue


def customer_birthday_input() -> str:
    while True:
        customer_birthday = input(" Please Enter Your Birthday (YYYY-MM-DD) >> ")
        pattern = r'^\d{4}-\d{2}-\d{2}$'
        match = re.search(pattern, str(customer_birthday))
        if match:
            return customer_birthday
        print(" Please Try Again >> ")
        continue


# ------------ input validations for Book ---------------

def book_id_input() -> int:
    while True:
        book_id = input(" Please Enter Book ID Number >> ")
        pattern = r'^\d{9}$'
        match = re.search(pattern, str(book_id))
        if match:
            return int(book_id)
        print(" Please Try Again >> ")
        continue


def book_name_input() -> str:
    while True:
        book_name = input(" Please Enter Book Name >> ")
        pattern = r'^[a-zA-Z]+(([\'\,\.\- ][a-zA-Z ])?[a-zA-Z]*)*$'
        match = re.search(pattern, str(book_name))
        if match:
            return book_name
        print(" Please Try Again >> ")
        continue


def book_author_input() -> str:
    while True:
        book_author = input(" Please Enter Book Author Name >> ")
        pattern = r'^[a-zA-Z]+(([\'\,\.\- ][a-zA-Z ])?[a-zA-Z]*)*$'
        match = re.search(pattern, str(book_author))
        if match:
            return book_author
        print(" Please Try Again >> ")
        continue


def book_year_input() -> int:
    while True:
        book_year = input(" Please Enter Book's Year The Of Publish (YYYY) >> ")
        pattern = r'^\d{4}$'
        match = re.search(pattern, str(book_year))
        if match:
            return int(book_year)
        print(" Please Try Again >> ")
        continue


def book_type_input() -> int:
    while True:
        book_type = input(" Please Enter Book Type (for future return date) (1/2/3)  >> ")
        pattern = r'^\d{1}$'
        match = re.search(pattern, str(book_type))
        if match:
            return int(book_type)
        print(" Please Try Again >> ")
        continue

