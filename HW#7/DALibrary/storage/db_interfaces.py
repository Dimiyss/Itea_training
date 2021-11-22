"""Module with base abstract methods for work with data storage"""
from abc import ABC, abstractmethod


class BaseDB(ABC):
    """Class consists abstract method for work with storage"""

    @abstractmethod
    def save_books(self, books: str):
        """Method for save object book to storage"""
        pass

    @abstractmethod
    def load_books(self):
        """Method for load book from storage"""
        pass

    @abstractmethod
    def save_readers(self, readers: list):
        """Method for save object reader to storage"""
        pass

    @abstractmethod
    def load_readers(self):
        """Method for load reader from storage"""
        pass
