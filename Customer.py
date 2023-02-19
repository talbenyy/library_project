from datetime import datetime


class Customer:
    def __init__(self, customer_id: int, name: str, address: str, email: str, birthday: str):
        self.customer_id = customer_id
        self.name = name
        self.address = address
        self.email = email
        self.birthday = datetime.strptime(birthday, '%Y-%m-%d')

    def get_id(self) -> int:
        return self.customer_id

    def set_id(self, customer_id: int):
        self.customer_id = customer_id

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str):
        self.name = name

    def get_address(self) -> str:
        return self.address

    def set_address(self, address: str):
        self.address = address

    def get_email(self) -> str:
        return self.email

    def set_email(self, email: str):
        self.email = email

    def get_birthday(self) -> datetime.date:
        return self.birthday

    def set_birthday(self, birthday: datetime.date):
        self.birthday = birthday

    def __str__(self):
        return f"{self.customer_id} - {self.name} ({self.email})"

    def __repr__(self):
        return f"{self.customer_id} - {self.name} ({self.email})"
