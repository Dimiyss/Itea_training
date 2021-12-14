from ..storage.sqlstorage.storage_base import Base
from sqlalchemy import Column, Integer, Text, SmallInteger, ForeignKey
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    email = Column(Text, nullable=False)
    psw_hash = Column(Text, nullable=False)

    reader_id = Column(Integer, ForeignKey('reader.id'), nullable=False)
    reader = relationship('Reader', backref='user')

    def __init__(self, email: str, psw_hash: str, reader_id: int):
        self.email = email
        self.psw_hash = psw_hash
        self.reader_id = reader_id

    def __repr__(self):
        return f'Reader {self.reader} has email {self.email} and psw_hash {self.psw_hash}'