"""The Reader Module"""
from ..storage.sqlstorage.storage_base import Base
from sqlalchemy import Column, Integer, Text, SmallInteger, Boolean
from sqlalchemy.orm import relationship


class Reader(Base):
    """Class that describe reader in library"""
    __tablename__ = 'reader'

    id = Column(Integer, primary_key=True)
    first_name = Column(Text, nullable=False)
    second_name = Column(Text, nullable=False)
    age = Column(SmallInteger, nullable=False)
    is_active = Column(Boolean, nullable=False)

    def __init__(self, first_name: str, second_name: str, age: int, is_active: bool = True):
        self.first_name = first_name
        self.second_name = second_name
        self.age = age
        self.is_active = is_active

    def to_dict(self) -> dict:
        """
        Method than convert cls object to dict
        :return: dict
        """
        return {
            "id": self.id,
            "first_name": self.first_name,
            "second_name": self.second_name,
            "age": self.age,
            "is_active": self.is_active
        }

    @classmethod
    def from_dict(cls, obj_attr_dict: dict):
        return cls(
            obj_attr_dict['first_name'],
            obj_attr_dict['second_name'],
            obj_attr_dict['age'],
            obj_attr_dict['is_active']
        )

    def get_id(self) -> int:
        return self.id

    def deactivate(self):
        self.is_active = False

    def __str__(self):
        return f'{self.id}_{self.first_name} {self.second_name}'

    def __repr__(self):
        return f'{self.id}_{self.first_name} {self.second_name}'
