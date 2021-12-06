from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Text, create_engine
from sqlalchemy.orm import Session

Base = declarative_base()


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


engine = create_engine('postgresql://postgres:pgpwd4habr@localhost:5432/postgres')
session = Session(engine)

Base.metadata.create_all(engine)

user_anna = User('Anna', 15)

# session.add(user_anna)
# session.commit()

# session.add_all([
#     User('Ivan', 20),
#     User('Petr', 25),
#     User('Emma', 30),
#     User('Jack', 35)
# ])
#
# session.commit()

# for user in session.query(User):
#     print(user)


# 1. session.query(User) = (select * from users) -> list[User]

# users_older_20 = session.query(User).filter(User.age > 20).all()
# for user in users_older_20:
#     print(user)


# print(session.query(User).filter(User.age > 20).first())

# print(session.query(User).filter(User.age > 40).one())


# print(session.query(User).filter_by(age='>35').first())


# print(session.query(User).filter(User.age > 20).filter(User.age <30).first())

user_emma = session.query(User).filter(User.name == 'Emma').one()
# print(user_emma)
# user_emma.age = 29
# session.commit()
#
# user_emma = session.query(User).filter(User.name == 'Emma').one()
# print(user_emma)


session.delete(user_emma)
session.commit()


