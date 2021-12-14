"""Module with base abstract methods for work with data storage"""
from abc import ABC, abstractmethod


class BaseDB(ABC):
    """Class consists abstract method for work with storage"""

    @abstractmethod
    def first_run(self):
        pass

    @abstractmethod
    def save_books(self, books: str):
        """Method for save object book to storage"""
        pass

    @abstractmethod
    def load_books(self, is_all, is_available):
        """Method for load book from storage"""
        pass

    @abstractmethod
    def update_book(self, book_id: int, reader_id: int, is_return: bool) -> bool:
        pass

    @abstractmethod
    def delete_book(self, book_id: int) -> str:
        pass

    @abstractmethod
    def load_reader_books(self, reader_id: int):
        pass

    @abstractmethod
    def get_reader_by_id(self, reader_id):
        pass

    @abstractmethod
    def get_book_by_id(self, book_id: int):
        pass

    @abstractmethod
    def save_readers(self, readers: list):
        """Method for save object reader to storage"""
        pass

    @abstractmethod
    def load_reader_book(self, reader_id):
        pass

    @abstractmethod
    def delete_reader(self, reader_id: int):
        pass

    @abstractmethod
    def load_readers(self):
        """Method for load reader from storage"""
        pass
