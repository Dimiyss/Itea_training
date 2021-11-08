"""The Book Module"""
from typing import Any


class Book:
    """Class that describe book in library"""
    count = 0

    def __init__(
            self,
            title: str,
            author: str,
            published_date: str,
            genre: str, id: int = None,
            current_place: int = 0
    ):
        Book.count += 1
        self.__id = id if id else Book.count
        self.__title = title
        self.__author = author
        self.__published_date = published_date
        self.__genre = genre
        self.__current_place = current_place  # 0 - book in library, else - reader id

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

    def to_dict(self) -> dict:
        """
        Method than convert cls object to dict
        :return: dict
        """
        return {
            "id": self.__id,
            "title": self.__title,
            "author": self.__author,
            "published_date": self.__published_date,
            "genre": self.__genre,
            "current_place": self.__current_place
        }

    @classmethod
    def from_dict(cls, obj_attr_dict: dict):
        return cls(
            obj_attr_dict['title'],
            obj_attr_dict['author'],
            obj_attr_dict['published_date'],
            obj_attr_dict['genre'],
            obj_attr_dict['id'],
            obj_attr_dict['current_place']
        )

    def __str__(self):
        return f'{self.__id}:{self.__title}'

    def __repr__(self):
        return f'{self.__id}:{self.__title}'
