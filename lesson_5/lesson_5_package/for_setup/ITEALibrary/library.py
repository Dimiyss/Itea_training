from .utils.book import Book
from .utils.reader import Reader


class Library:
    def __init__(self):
        self.books = []
        self.readers = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)
        print('book added')