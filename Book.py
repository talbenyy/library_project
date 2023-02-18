class Book:
    def __init__(self, book_id, name, author, year_published):
        self.book_id = book_id
        self.name = name
        self.author = author
        self.year_published = year_published

    def get_book_id(self):
        return self.book_id

    def set_book_id(self, book_id):
        self.book_id = book_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_author(self):
        return self.author

    def set_author(self, author):
        self.author = author

    def get_year_published(self):
        return self.year_published

    def set_year_published(self, year_published):
        self.year_published = year_published

    def __str__(self):
        return f"{self.book_id} - {self.name} by {self.author} ({self.year_published})"

    def __repr__(self):
        return f"{self.book_id} - {self.name} by {self.author} ({self.year_published})"
