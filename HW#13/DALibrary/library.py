"""The Library Module"""
from .units.book import Book
from .units.reader import Reader
from .storage.sqlstorage.storage_method import AlchemyStorage as DataBase
from typing import Any


class Library:
    """Class that describe library"""
    def __init__(self, storage: DataBase, book_list: list = None, reader_list: list = None):
        self.__storage = storage

    def add_book(self, book: Book) -> str:
        """
        Method that add book to library book list
        :param book: New book object
        :return: result description string
        """
        res = self.__storage.save_books([book])
        if res:
            return f'Books successfully added to library'

        return 'Error in added books process'

    def delete_books(self, book_id_list: list) -> str:
        """Func that delete book form library

        :param book_id_list: List of Book object identifier
        :return: result description string
        """
        msg = ''

        for book_id in book_id_list:
            msg += f'{self.delete_book(book_id)}\n'

        return msg

    def delete_book(self, book_id: int) -> str:
        """
        Func that delete book form library
        :param book_id: Book object identifier
        :return: result description string
        """
        book = self.__get_book_by_id(book_id)
        if book is None:
            return f'Book with id {book_id} not exist.'
        else:
            self.__storage.delete_book(book_id)
            return f'Book with id {book_id} was deleted from library.'

    def give_book(self, book_id_list: list, reader_id: int) -> str:
        """The function of giving a book to the reader.

        :param book_id_list: List of Book identifiers
        :param reader_id: Reader identifier
        :return: result description string
        """
        msg = ''
        for book_id in book_id_list:
            msg += f'{self.give_book(book_id, reader_id)}'

        return msg

    def give_book(self, book_id: int, reader_id: int) -> str:
        """The function of giving a book to the reader.

        :param book_id: Book identifier
        :param reader_id: Reader identifier
        :return: result description string
        """
        reader = self.__storage.get_reader_by_id(reader_id)
        if reader is None:
            return f'Reader with id {reader_id} is not exists'

        book = self.__get_book_by_id(book_id)

        if book is None:
            return f'Book with id {book_id} is not exists'

        # if book.get_current_place() is not None:
        #     return f'Book with {book_id} is not available'

        res = self.__storage.update_book(book_id, reader_id)

        if not res:
            return f'Error to give book {book} to reader {reader}'

        return f'Book {book} successfully gave to reader {reader}'

    def return_books(self, book_id_list: list) -> str:
        """The function of returning a book to the library

        :param book_id_list: List of book identifiers
        :return: result description string
        """
        msg = ''
        for book_id in book_id_list:
            msg += f'{self.give_book(book_id)}'

        return msg

    def return_book(self, book_id: int) -> str:
        """
        The function of returning a book to the library
        :param book_id:
        :return: result description string
        """
        book = self.__get_book_by_id(book_id)

        if not book:
            return f'Book with id {book_id} is not exists'

        res = self.__storage.update_book(book_id, None)

        if not res:
            return f'Error return book {book}'

        return f'Book {book} successfully returned to library'

    def __get_book_by_id(self, book_id: int) -> Any:
        """
        Func that find book by book identifier
        :param book_id: unique book object identifier
        :return: book object if found else return None
        """
        return self.__storage.get_book_by_id(book_id)

    def add_reader(self, reader: Reader) -> str:
        """
        Method that add reader to library reader list
        :param reader: New reader object
        :return: result description string
        """

        self.__storage.save_readers([reader])

        return f'Reader {reader} successfully added to library'

    def get_reader_list(self) -> list:
        return self.__reader_list

    def get_book_list(self) -> list:
        return self.__storage.load_books(is_all=True)

    def get_available_book_list(self) -> list:
        """
        The function of found all available in the library (current_place == 0)
        :return: list of book object
        """
        return self.__storage.load_books(is_all=False, is_available=True)

    def get_busy_book_list(self) -> list:
        """
        The function of found all busy in the library (reader_id = Null)
        :return: list of book object
        """
        return self.__storage.load_books(is_all=False, is_available=False)

    def get_reader_books(self, reader_id: int) -> list:
        """Method that return all book that take by reader

        :param reader_id:reader identifier
        :return: list of Book object
        """
        reader = self.__storage.get_reader_by_id(reader_id)

        if reader is None:
            return None

        return reader.book
