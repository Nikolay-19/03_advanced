class Book:
    def __init__(self, content):
        self.content = content


class Formatter:
    @staticmethod
    def format(book):
        return book.content


class Printer:
    @staticmethod
    def get_book(book):
        return Formatter.format(book)
