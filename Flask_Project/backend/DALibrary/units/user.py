from ..storage.sqlstorage.storage_base import Base
from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship
from flask_login import UserMixin

from werkzeug.security import generate_password_hash, check_password_hash


class User(Base, UserMixin):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    email = Column(Text, nullable=False, unique=True)
    psw_hash = Column(Text, nullable=False)

    reader_id = Column(Integer, ForeignKey('reader.id'), nullable=False)
    reader = relationship('Reader', backref='user')

    def __init__(self, email: str, psw_hash: str, reader_id: int):
        self.email = email
        self.psw_hash = generate_password_hash(psw_hash)
        self.reader_id = reader_id

    def __repr__(self):
        return f'Reader {self.reader} has email {self.email} and psw_hash {self.psw_hash}'

    def check_psw(self, psw):
        return check_password_hash(self.psw_hash, psw)

    def get_id(self):
        return self.id

    def get_name(self):
        return self.reader.first_name

    def get_reader_id(self):
        return self.reader_id
