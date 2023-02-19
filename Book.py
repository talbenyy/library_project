class Book:
    def __init__(self, book_id: int, name: str, author: str, year_published: int, book_type: int):
        self.book_id = book_id
        self.name = name
        self.author = author
        self.year_published = year_published
        self.book_type = book_type

    def get_book_id(self) -> int:
        return self.book_id

    def set_book_id(self, book_id: int):
        self.book_id = book_id

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str):
        self.name = name

    def get_author(self) -> str:
        return self.author

    def set_author(self, author: str):
        self.author = author

    def get_year_published(self) -> int:
        return self.year_published

    def set_year_published(self, year_published: int):
        self.year_published = year_published

    def get_book_type(self) -> int:
        return self.book_type

    def set_book_type(self, book_type: int):
        self.book_type = book_type

    def __str__(self) -> str:
        return f"{self.book_id} - {self.name} by {self.author} ({self.year_published})"

    def __repr__(self) -> str:
        return f"{self.book_id} - {self.name} by {self.author} ({self.year_published})"
