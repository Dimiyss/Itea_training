from abc import ABC

import psycopg2
from .db_interfaces import BaseDB
from psycopg2.extras import DictCursor, NamedTupleCursor
from ..units.book import Book
from ..units.reader import Reader
import storage.sql_templates as tmpl


class PsyCopgDB(BaseDB, ABC):
    """Class for psycopg2 methods to library"""
    def __init__(self, db_connection_config: str, book_table_name: str = 'book', reader_table_name: str = 'reader'):
        self.__db_connection_config = db_connection_config
        self.__book_table_name = book_table_name
        self.__reader_table_name = reader_table_name
        self.first_run()

    def __create_connection(self):
        """Open connection to DB"""
        conn = psycopg2.connect(self.__db_connection_config)

        return conn

    def first_run(self):
        """Create empty tables in DB"""
        connection = self.__create_connection()
        self.__execute_query(connection, tmpl.CREATE_BOOK_TABLE)
        self.__execute_query(connection, tmpl.CREATE_READER_TABLE)
        connection.commit()
        connection.close()

    @staticmethod
    def __execute_query(conn: psycopg2, query: str, need_return: bool = False):
        """Internal method for query executing

        :param conn: psycopg2 object connection
        :param query: executed query
        :param need_return: flag that indicate if query result must retur to caller method
        """
        return_list = []
        with conn.cursor(cursor_factory=NamedTupleCursor) as cursor:
            cursor.execute(query)
            if need_return:
                for row in cursor:
                    return_list.append(row)

        return return_list

    def save_books(self, books: list) -> str:
        """Method for write books list objects in PG table

        :param books: list of books( object class Book)
        :return: result description string
        """
        if not books:
            msg = 'Nothing to write to db'
            return msg

        insert_values_list = []
        for book in books:
            dict_book = book.to_dict()
            if not dict_book.get('reader_id') or dict_book.get('reader_id') == 'None':
                dict_book['reader_id'] = 'null'

            insert_values_list.append(tmpl.BOOK_VALUES.render(dict_book))

        print(insert_values_list)

        connection = self.__create_connection()
        self.__execute_query(
            connection,
            tmpl.INSERT_TEMPLATE.render(
                table_name=self.__book_table_name,
                columns=tmpl.BOOK_COLUMNS,
                insert_values=','.join(insert_values_list))
        )
        connection.commit()
        connection.close()
        msg = 'Books successfully saved to DB'

        return msg

    def update_book(self, book_id: int, reader_id: int, is_return: bool) -> str:
        """Method that update book in DB

        :param book_id: the book identifier in database
        :param reader_id: the reader identifier in database
        :param is_return: flag that indicate that book will return to Library
        """
        if is_return:
            query = tmpl.UPDATE_TEMPLATE.render(book_id=book_id, reader_id='null')
        else:
            query = tmpl.UPDATE_TEMPLATE.render(book_id=book_id, reader_id=reader_id)

        connection = self.__create_connection()

        self.__execute_query(connection, query)

        connection.commit()
        connection.close()

        return True

    def delete_book(self, book_id: int) -> str:
        """Method that delete book in DB

        :param book_id: the book identifier in database
        :return: string
        """

        query = tmpl.DELETE_TEMPLATE.render(table_name=self.__book_table_name, condition=f'id = {book_id}')
        connection = self.__create_connection()

        self.__execute_query(connection, query)

        connection.commit()
        connection.close()

        return f'Book id = {book_id} successfully deleted'

    def load_books(self, is_all: bool, is_available: bool = False) -> list:
        """Method for load book from storage.

        :param is_all: flag if True then return all book (is_available - ignored)
        :param is_available: flag if is_available = True and is_all = False -> then return only available
                                  if is_available = False and is_all = False -> then return only busy
        :return: book list
        """
        if not is_all:
            if is_available:
                condition = 'reader_id is null'
            else:
                condition = 'reader_id is not null'
        else:
            condition = 'true'

        query = tmpl.SELECT_TEMPLATE.render(field_list='*', table_name=self.__book_table_name, condition=condition)
        connection = self.__create_connection()

        res = self.__execute_query(connection, query, True)

        connection.close()
        return_list = []

        for row in res:
            return_list.append(
                Book.from_dict(
                    dict(
                        id=row.id,
                        title=row.title,
                        author=row.author,
                        published_year=row.published_year,
                        genre=row.genre,
                        reader_id=row.reader_id
                    )
                )
            )

        return return_list

    def load_reader_books(self, reader_id: int):
        """Method that return all reader book.

        :param reader_id: reader identifier
        :return: list pf books
        """
        is_exist, _ = self.get_reader_by_id(reader_id)
        if not is_exist:
            return f'Reader with id = {reader_id} not exists'

        query = tmpl.SELECT_TEMPLATE.render(
            field_list='*',
            table_name=self.__book_table_name,
            condition=f'reader_id = {reader_id}'
        )
        connection = self.__create_connection()
        res = self.__execute_query(connection, query, True)
        connection.close()

        if len(res) == 0:
            return None

        return_list = []

        for row in res:
            return_list.append(
                Book.from_dict(
                    dict(
                        id=row.id,
                        title=row.title,
                        author=row.author,
                        published_year=row.published_year,
                        genre=row.genre,
                        reader_id=row.reader_id
                    )
                )
            )
        return return_list

    def get_reader_by_id(self, reader_id):
        """The method that return reader by id

        :param reader_id: reader identifier
        :return: object Reader or None
        """
        query = tmpl.SELECT_TEMPLATE.render(
            field_list='*',
            table_name=self.__reader_table_name,
            condition=f'id = {reader_id}'
        )
        connection = self.__create_connection()
        res = self.__execute_query(connection, query, True)
        connection.close()

        if len(res) == 0:
            return False, None

        reader = Reader.from_dict(
            dict(
                id=res[0].id,
                first_name=res[0].first_name,
                second_name=res[0].second_name,
                age=res[0].age,
                is_active=res[0].is_active
            )
        )

        return True, reader

    def get_book_by_id(self, book_id: int):
        """Method that found book in DB by book_id.

        :param book_id:the book identifier
        :return: Object Book if found or None
        """
        query = tmpl.SELECT_TEMPLATE.render(
            field_list='*',
            table_name=self.__book_table_name,
            condition=f'id = {book_id}'
        )
        connection = self.__create_connection()
        res = self.__execute_query(connection, query, True)
        connection.close()

        if len(res) == 0:
            return False, None

        book = Book.from_dict(
            dict(
                id=res[0].id,
                title=res[0].title,
                author=res[0].author,
                published_year=res[0].published_year,
                genre=res[0].genre,
                reader_id=res[0].reader_id
            )
        )

        return True, book

    def save_readers(self, readers: list) -> str:
        """Method for write reader list objects in PG table

        :param readers: list of readers( object class Book)
        :return: result description string
        """
        if not readers:
            msg = 'Nothing to write to DB'
            return msg

        connection = self.__create_connection()
        insert_values_list = []
        for reader in readers:
            print(reader)
            insert_values_list.append(tmpl.READER_VALUES.render(reader))

        res = self.__execute_query(
            connection,
            tmpl.INSERT_TEMPLATE.render(table_name=self.__reader_table_name,
                                   columns=tmpl.READER_COLUMNS,
                                   insert_values=','.join(insert_values_list))
        )
        # if not res:
        #     connection.rollback()
        #     msg = 'Error insert date to DB'
        #     status = False
        # else:
        connection.commit()
        msg = 'Reader successfully saved to DB'

        connection.close()
        return msg

    def load_readers(self):
        """Method for load readers from storage

        :return: reader list
        """
        query = tmpl.SELECT_TEMPLATE.render(field_list='*', table_name=self.__reader_table_name, condition='true')
        connection = self.__create_connection()

        res = self.__execute_query(connection, query)

        connection.close()

        return res

    def load_reader_book(self, reader_id):
        """Return all books that take user"""
        query = tmpl.SELECT_TEMPLATE.render(
            field_list='*',
            table_name=self.__book_table_name,
            condition=f'reader_id = {reader_id}'
        )
        connection = self.__create_connection()

        res = self.__execute_query(connection, query, True)

        connection.close()
        return_list = []

        for row in res:
            return_list.append(
                dict(
                    id=row.id,
                    title=row.title,
                    author=row.author,
                    published_year=row.published_year,
                    genre=row.genre,
                    reader_id=row.reader_id
                )
            )

        return return_list

    def delete_reader(self, reader_id: int):
        """Method that delete book in DB

        :param reader_id: the book identifier in database
        """
        query = tmpl.DELETE_TEMPLATE.render(table_name=self.__reader_table_name, condition=f'id = {reader_id}')
        connection = self.__create_connection()

        self.__execute_query(connection, query)

        connection.commit()
        connection.close()


if __name__ == '__main__':

    config = "dbname=postgres user=postgres password=pgpwd4habr host=localhost port=5432"
    print(config)
    db = PsyCopgDB(config)
    # dict = {
    #     'title': 'Book #4',
    #     'author': 'Author #4',
    #     'published_year': 2021,
    #     'genre': 'Doc',
    #     'reader_id': 222
    # }
    # dict_1 = {
    #     'title': 'Book #5',
    #     'author': 'Author #6',
    #     'published_year': 2020,
    #     'genre': 'Doc'
    # }
    # book_list = [dict, dict_1]
    #
    # db.first_run()
    # db.save_books(book_list)
    print(db.load_books(is_all=True, is_available=False))
