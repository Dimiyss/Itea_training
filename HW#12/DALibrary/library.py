"""The Library Module"""
from .units.book import Book
from .units.reader import Reader
from .storage.psycop_db import PsyCopgDB as DataBase
from typing import Any


class Library:
    """Class that describe library"""
    def __init__(self, storage: DataBase, book_list: list = None, reader_list: list = None):
        self.__storage = storage
        #self.__book_list = book_list if book_list else []
        #self.__reader_list = reader_list if reader_list else []

    def add_book(self, book: Book) -> str:
        """
        Method that add book to library book list
        :param book: New book object
        :return: result description string
        """
        print(book)
        msg = self.__storage.save_books([book])

        return msg

    def delete_book(self, book_id: int) -> str:
        """
        Func that delete book form library
        :param book_id: Book object identifier
        :return: result description string
        """
        _, book = self.__get_book_by_id(book_id)
        if book is None:
            return f'Book with id {book_id} not exist.'
        else:
            self.__storage.delete_book(book_id)
            return f'Book with id {book_id} was deleted from library.'

    def give_book(self, book_id: int, reader_id: int) -> str:
        """
        The function of giving a book to the reader
        :param book_id: Book identifier
        :param reader_id: Reader identifier
        :return: result description string
        """
        reader_exists, reader = self.__storage.get_reader_by_id(reader_id)
        if not reader_exists:
            return f'Reader with id {reader_id} is not exists'

        book_exists, book = self.__get_book_by_id(book_id)

        if not book_exists:
            return f'Book with id {book_id} is not exists'

        if book.get_current_place() is not None:
            return f'Book with {book_id} is not available'

        self.__storage.update_book(book_id, reader_id, False)

        return f'Book {book} successfully gave to reader {reader}'

    def return_book(self, book_id: int) -> str:
        """
        The function of returning a book to the library
        :param book_id:
        :return: result description string
        """
        book_exists, book = self.__get_book_by_id(book_id)

        if not book_exists:
            return f'Book with id {book_id} is not exists'

        self.__storage.update_book(book_id, 0, True)

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

        self.__storage.save_readers([reader.to_dict()])

        return f'Reader {reader} successfully added to library'

    def __get_reader_by_id(self, reader_id: int) -> None:
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

        return self.__storage.load_reader_books(reader_id)

    def sorted_book(self, sort_key, is_reverse=False) -> list:
        """
        The function for sorting book list in library
        :param sort_key: attribute on which list would be sorted
        :param is_reverse: flag indicate reverse way of sort
        :return:
        """
        return sorted(self.__book_list, key=lambda x: x.get_attribute_value(sort_key), reverse=is_reverse)

    def __repr__(self):
        return f'All books in lib: {self.__book_list}\nAll readers: {self.__reader_list}'

    def __str__(self):
        return f'All books in lib: {self.__book_list}\nAll readers: {self.__reader_list}'

    def is_reader(self, reader_id: int) -> bool:
        """
        The method that check is reader exist
        :param reader_id: unique reader object identifier
        :return: If reader exist - True else False
        """
        if self.__get_reader_by_id(reader_id):
            return True
        else:
            return False

    def __save_books(self):
        """Method save books list to DB"""
        self.__storage.save_books([book for book in self.__book_list])

    def __save_readers(self):
        """Method save readers list to DB"""
        self.__storage.save_readers([reader.to_dict() for reader in self.__reader_list])
