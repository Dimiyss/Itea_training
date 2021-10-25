from abc import ABCMeta, abstractmethod, ABC


class ConnectorDB(ABC):
    # __metaclass__ = ABCMeta

    def __init__(self):
        print('Connection')

    @abstractmethod
    def read_from_db(self):
        # print('read from DB')
        pass

    @abstractmethod
    def write_to_db(self):
        # print('write_to_db')
        pass


class ConnectorDBPostgreSQL(ConnectorDB):
    def read_from_db(self):
        print('read from DB (PostgreSQL)')

    def write_to_db(self):
        print('write_to_db (PostgreSQL)')


class ConnectorDBNoSQL(ConnectorDB):
    def read_from_db(self):
        print('read from DB (NoSQL)')

    def write_to_db(self):
        print('write_to_db (NoSQL)')


connection = ConnectorDBNoSQL()

connection.read_from_db()

connection.write_to_db()

