class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        if book not in self.books:
            self.books.append(book)

    def find_book(self, book):
        if book in self.books:
            return book.name
