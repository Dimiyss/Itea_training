"""The library"""
from library_DA.utils.book import Book
from library_DA.utils.reader import Reader
from typing import Any


class Library:
    """Class that describe library"""
    def __init__(self, book_list: list = None, reader_list: list = None):
        self.__book_list = [] if book_list is None else book_list
        self.__reader_list = [] if reader_list is None else reader_list

    def add_book(self, book: Book) -> str:
        """
        Method that add book to library book list
        :param book: New book object
        :return: result description string
        """
        self.__book_list.append(book)
        return f'Book {book} successfully added to library'

    def add_reader(self, reader: Reader) -> str:
        """
        Method that add reader to library reader list
        :param reader: New reader object
        :return: result description string
        """
        self.__reader_list.append(reader)
        return f'Reader {reader} successfully added to library'

    def get_book_by_id(self, book_id: int) -> Any:
        """
        Func that find book by book identifier
        :param book_id: unique book object identifier
        :return: book object if found else return None
        """
        for book in self.__book_list:
            if book.get_id() == book_id:
                return book
        else:
            print(f'Book with id {book_id} not exist')
            return None

    def get_reader_by_id(self, reader_id: int) -> None:
        """
        Func that find reader by reader identifier
        :param reader_id: unique reader object identifier
        :return: reader object if found else return None
        """
        for reader in self.__reader_list:
            if reader.get_id() == reader_id:
                return reader
        else:
            print(f'Reader with id {reader_id} not exist')
            return None

    def delete_book(self, book_id: int) -> str:
        """
        Func that delete book form library
        :param book_id: Book object identifier
        :return: result description string
        """
        book = self.get_book_by_id(book_id)
        if book is None:
            return f'Book with id {book_id} not exist'
        else:
            self.__book_list.remove(book)
            return f'Book with id {book_id} was deleted from library'

    def give_book(self, book_id: int, reader_id: int) -> str:
        """
        The function of giving a book to the reader
        :param book_id: Book identifier
        :param reader_id: Reader identifier
        :return: result description string
        """
        if self.get_reader_by_id(reader_id) is None:
            return f'Reader with id {reader_id} is not exists'

        book = self.get_book_by_id(book_id)

        if book is None:
            return f'Book with id {book_id} is not exists'

        if book.get_current_place() != 0:
            return f'Book with {book_id} is not available'

        book.set_current_place(reader_id)

        return f'Book {book} successfully gave to reader'

    def return_book(self, book_id: int) -> str:
        """
        The function of returning a book to the library
        :param book_id:
        :return: result description string
        """
        book = self.get_book_by_id(book_id)

        if book is None:
            return f'Book with id {book_id} is not exists'

        book.set_current_place(0)
        return f'Book {book} successfully returned to library'

    def get_book_list(self) -> list:
        return self.__book_list

    def get_available_book_list(self) -> list:
        """
        The function of found all available in the library (current_place == 0)
        :return: list of book object
        """
        available_book = []
        for book in self.__book_list:
            if book.get_current_place() == 0:
                available_book.append(book)

        return available_book

    def get_busy_book_list(self) -> list:
        """
        The function of found all busy in the library (current_place != 0)
        :return: list of book object
        """
        busy_book = []
        for book in self.__book_list:
            if book.get_current_place != 0:
                busy_book.append(book)

        return busy_book

    def sorted_book(self, sort_key, is_reverse=False) -> list:
        """
        The function for sorting book list in library
        :param sort_key: attribute on which list would be sorted
        :param is_reverse: flag indicate reverse way of sort
        :return:
        """
        return sorted(self.__book_list, key=lambda x: x.__getattribute__(sort_key), reverse=is_reverse)

    def __repr__(self):
        return f'All books in lib: {self.__book_list}\nAll readers: {self.__reader_list}'

    def __str__(self):
        return f'All books in lib: {self.__book_list}\nAll readers: {self.__reader_list}'
