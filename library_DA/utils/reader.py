"""The Reader Module"""
from datetime import datetime


class Reader:
    """Class that describe reader in library"""
    count = 0

    def __init__(self, first_name, second_name):
        Reader.count += 1
        self.__id = Reader.count
        self.__first_name = first_name
        self.__second_name = second_name
        self.__created_date = datetime.today().strftime('%Y-%m-%d-%H:%M:%S')
        self.__is_active = True

    def get_id(self) -> int:
        return self.__id

    def deactivate(self):
        self.__is_active = False

    def __str__(self):
        return f'{self.__id}_{self.__first_name} {self.__second_name}'

    def __repr__(self):
        return f'{self.__id}_{self.__first_name} {self.__second_name}'
