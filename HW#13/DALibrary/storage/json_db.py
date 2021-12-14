"""Module for work with file data base in JSON format"""
import json
from ..storage.db_interfaces import BaseDB
from ..units.book import Book
from ..units.reader import Reader


class JsonDB(BaseDB):
    """Class for work with file DB"""
    def __new__(cls, storage_path):
        if not hasattr(cls, 'instance'):
            cls.instance = super(JsonDB, cls).__new__(cls)
        return cls.instance

    def __init__(self, storage_path: str):
        self.storage_path = storage_path

    def __write_file(self, file_name: str, content: list) -> str:
        """
        The method for write data into file
        :param file_name: file name (enum books or reader)
        :param content: list of objects that would be saved into the file
        :return: result description string
        """
        with open((self.storage_path + file_name), 'w') as file:
            for element in content:
                file.write(json.dumps(element) + '\n')

        return f'Write success'

    def __read_from_file(self, file_name: str) -> list:
        """
        The method for read data from file
        :param file_name: file name (enum books or reader)
        :return: list of data elements
        """
        objs_list = []
        with open((self.storage_path + file_name), 'r') as file:
            for line in file:
                objs_list.append(line)

        return objs_list

    def save_books(self, books: list) -> str:
        """
        Method for write books list objects in file in JSON format
        :param books: list of books( object class Book)
        :return: result description string
        """
        if not books:
            return f'Nothing to write to db'

        self.__write_file('books.json', [book.to_dict() for book in books])

        return f'Books successfully saved to db'

    def save_readers(self, readers: list) -> str:
        """
        Method for write books list objects in file in JSON format
        :param readers: list of readers( object class Reader)
        :return: result description string
        """
        if not readers:
            return f'Nothing to write to db'

        self.__write_file('readers.json', [reader.to_dict() for reader in readers])

        return f'Books successfully saved to db'

    def load_books(self) -> list:
        """
        Method for load books from file
        :return: books
        """
        books_list = self.__read_from_file('books.json')

        if not books_list:
            return []

        books = []

        for book in books_list:
            books.append(Book.from_dict(json.loads(book)))

        return books

    def load_readers(self) -> list:
        """
        Method for load readers from file
        :return: readers
        """
        readers_list = self.__read_from_file('readers.json')

        if not readers_list:
            return []

        readers = []

        for reader in readers_list:
            readers.append(Reader.from_dict(json.loads(reader)))

        return readers
