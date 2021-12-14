from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Text, create_engine
from sqlalchemy.orm import Session

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    surname = Column(Text)
    age = Column(Integer, nullable=False)

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'name: {self.name}, age: {self.age}'


engine = create_engine('postgresql://postgres:123@localhost:5432/postgres')
session = Session(engine)

Base.metadata.create_all(engine)

# session.add_all([
#     User('Ivan', 20),
#     User('Petr', 25),
#     User('Emma', 30),
#     User('Jack', 35),
# ])
# session.commit()
