"""The Book Module"""
from typing import Any


class Book:
    """Class that describe book in library"""
    count = 0

    def __init__(self, title, author, published_date, genre):
        Book.count += 1
        self.__id = Book.count
        self.__title = title
        self.__author = author
        self.__published_date = published_date
        self.__genre = genre
        self.__current_place = 0  # 0 - library, else - reader id

    def get_id(self) -> int:
        return self.__id

    def get_current_place(self):
        return self.__current_place

    def set_current_place(self, reader_id):
        self.__current_place = reader_id

    def get_attribute_value(self, name: str) -> Any:
        """
        The function for return object attribute value by name
        :param name: attribute name
        :return: attribute valuer
        """
        if name == 'title':
            return self.__title
        if name == 'published_date':
            return self.__published_date
        if name == 'author':
            return self.__author

    def __str__(self):
        return f'{self.__id}:{self.__title}'

    def __repr__(self):
        return f'{self.__id}:{self.__title}'
