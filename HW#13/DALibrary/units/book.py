"""The Book Module"""
from typing import Any


class Book:
    """Class that describe book in library"""
    count = 0

    def __init__(
            self,
            title: str,
            author: str,
            published_year: str,
            genre: str,
            _id: int = None,
            reader_id: int = None
    ):
        Book.count += 1
        self.__id = _id if _id else Book.count
        self.__title = title
        self.__author = author
        self.__published_year = published_year
        self.__genre = genre
        self.__reader_id = reader_id  # None - book in library, else - reader id

    def get_id(self) -> int:
        return self.__id

    def get_current_place(self):
        return self.__reader_id

    def set_current_place(self, reader_id):
        self.__reader_id = reader_id

    def get_attribute_value(self, name: str) -> Any:
        """
        The function for return object attribute value by name
        :param name: attribute name
        :return: attribute valuer
        """
        if name == 'title':
            return self.__title
        if name == 'published_date':
            return self.__published_year
        if name == 'author':
            return self.__author

    def to_dict(self) -> dict:
        """
        Method than convert cls object to dict
        :return: dict
        """
        return {
            "title": self.__title,
            "author": self.__author,
            "published_year": self.__published_year,
            "genre": self.__genre,
            "reader_id": self.__reader_id
        }

    @classmethod
    def from_dict(cls, obj_attr_dict: dict):
        return cls(
            obj_attr_dict['title'],
            obj_attr_dict['author'],
            obj_attr_dict['published_year'],
            obj_attr_dict['genre'],
            obj_attr_dict['id'],
            obj_attr_dict['reader_id']
        )

    def __str__(self):
        return f'{self.__id}:{self.__title}'

    def __repr__(self):
        return f'{self.__id}:{self.__title}'
