from sqlalchemy import Column, Integer, Text
from ex_2_base_class import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    age = Column(Integer, nullable=False)

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'name: {self.name}, age: {self.age}'