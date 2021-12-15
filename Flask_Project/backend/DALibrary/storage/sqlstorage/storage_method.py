from ..db_interfaces import BaseDB
from .storage_base import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from ...units.book import Book
from ...units.reader import Reader
from ...units.user import User


class AlchemyStorage(BaseDB):
    """Class consists method for work with storage """

    def __init__(
            self,
            db_user,
            db_password,
            db_name,
            db_address='localhost',
            db_port=5432,
            dialect='postgresql'
    ):

        self.__engine = create_engine(f'{dialect}://{db_user}:{db_password}@{db_address}:{db_port}/{db_name}')

        Base.metadata.create_all(self.__engine)
        self.session = Session(self.__engine)

    def save_books(self, books: list) -> bool:
        """Method for save object book to storage

        :param books: list of Book object
        :return: True or False
        """
        if len(books) == 0:
            return False

        for book in books:
            self.session.add(book)

        self.session.commit()

        return True

    def load_books(self, is_all: bool, is_available: bool = False) -> list:
        """Method for load book from storage

        :param is_all: need return all books
        :param is_available: return only available ( if is_all = False)
        :return: list Book objects or None
        """
        if is_all:
            return self.session.query(Book).all()

        if is_available:
            return self.session.query(Book).filter_by(reader_id=None).all()

        if not is_available:
            return self.session.query(Book).filter(Book.reader_id is not None).all()

    def update_book(self, book_id: int, reader_id: int) -> bool:
        """Method that update book in DB

        :param book_id: Book identifier
        :param reader_id: Reader identifier
        :return: bool
        """
        book = self.session.query(Book).filter_by(id=book_id).first()
        try:
            book.reader_id = reader_id
            self.session.commit()
        except:
            return False

        return True

    def delete_book(self, book_id: int) -> bool:
        """Method that update book in DB

        :param book_id: Book identifier
        :return: bool
        """
        book = self.session.query(Book).filter_by(id=book_id).first()
        try:
            self.session.delete(book)
            self.session.commit()
        except:
            return False

        return True

    # def load_reader_books(self, reader_id: int):
    #     """Method for return books that were taken by reader.
    #
    #     :param reader_id:Reader identifier
    #     :return: list of Book object or None
    #     """
    #     reader = self.session.query(Reader).filter_by(id=reader_id).first()
    #     return reader

    def get_reader_by_id(self, reader_id: int) -> list:
        """Method for return object Reader.

        :param reader_id:Reader identifier
        :return: object Reader
        """
        reader = self.session.query(Reader).filter_by(id=reader_id).first()
        return reader

    def get_book_by_id(self, book_id: int) -> list:
        """Method for return object Book.

        :param book_id:Book identifier
        :return: object Book
        """
        book = self.session.query(Book).filter_by(id=book_id).first()
        return book

    def save_reader(self, reader: Reader) -> int:
        """Method for save object book to storage

        :param reader: Reader object
        :return: created reader identifier
        """
        self.session.add(reader)

        self.session.commit()

        return reader.id

    def save_readers(self, readers: list) -> bool:
        """Method for save object book to storage

        :param readers: list of Reader object
        :return: True or False
        """
        if len(readers) == 0:
            return False

        for reader in readers:
            self.session.add(reader)

        self.session.commit()
        return True

    def delete_reader(self, reader_id: int) -> bool:
        """Method that update book in DB

        :param reader_id: Book identifier
        :return: bool
        """
        reader = self.session.query(Reader).filter_by(id=reader_id).first()
        try:
            self.session.delete(reader)
            self.session.commit()
        except:
            return False

        return True

    def load_readers(self):
        """Method for load reader from storage"""
        return self.session.query(Reader).all()

    def save_user(self, user: User) -> str:
        """Method for save object book to storage

        :param user: User object
        :return: string
        """
        self.session.add(user)

        self.session.commit()

        return f'{user} successfully added'

    def get_user_by_email(self, email):
        """Method  that find user by email.

        :param email: User email
        :return: User object
        """
        return self.session.query(User).filter_by(email=email).first()

    def get_user_by_id(self, user_id: int):
        """Method  that find user by email.

        :param user_id: User email
        :return: User object
        """
        return self.session.query(User).filter_by(id=user_id).first()
