from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship
from ex_2_base_class import Base


class Address(Base):
    __tablename__ = 'addresses'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    email = Column(Text, nullable=False, unique=True)

    user = relationship('User', backref='addresses')

    def __init__(self, user_id, email):
        self.user_id = user_id
        self.email = email

    def __str__(self):
        return f'User: {self.user}, address: {self.email}'
