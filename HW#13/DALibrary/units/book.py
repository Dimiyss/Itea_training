"""The Book Module"""
from typing import Any
from ..storage.sqlstorage.storage_base import Base
from sqlalchemy import Column, Integer, Text, SmallInteger, ForeignKey
from sqlalchemy.orm import relationship


class Book(Base):
    """Class that describe book in library"""
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True)
    title = Column(Text, nullable=False)
    author = Column(Text, nullable=False)
    published_year = Column(SmallInteger, nullable=False)
    genre = Column(Text, nullable=False)

    reader_id = Column(Integer, ForeignKey('reader.id'), nullable=True)
    reader = relationship('Reader', backref='book')

    def __init__(
            self,
            title: str,
            author: str,
            published_year: str,
            genre: str,
            reader_id: int = None
    ):
        self.title = title
        self.author = author
        self.published_year = published_year
        self.genre = genre
        self.reader_id = reader_id  # None - book in library, else - reader id

    def get_id(self) -> int:
        return self.id

    def get_current_place(self):
        return self.reader_id

    def set_current_place(self, reader_id):
        self.reader_id = reader_id

    def get_attribute_value(self, name: str) -> Any:
        """
        The function for return object attribute value by name
        :param name: attribute name
        :return: attribute valuer
        """
        if name == 'title':
            return self.title
        if name == 'published_date':
            return self.published_year
        if name == 'author':
            return self.author

    def to_dict(self) -> dict:
        """
        Method than convert cls object to dict
        :return: dict
        """
        return {
            "title": self.title,
            "author": self.author,
            "published_year": self.published_year,
            "genre": self.genre,
            "reader_id": self.reader_id
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

    def __repr__(self):
        return f'Book_id:{self.id},Title: {self.title}, Author: {self.author}, published: {self.published_year}'
