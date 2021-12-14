"""The Reader Module"""


class Reader:
    """Class that describe reader in library"""
    count = 0

    def __init__(self, first_name: str, second_name: str, age: int, id: int = None, is_active: bool = True):
        Reader.count += 1
        self.__id = id if id else Reader.count
        self.__first_name = first_name
        self.__second_name = second_name
        self.__age = age
        self.__is_active = is_active

    def to_dict(self) -> dict:
        """
        Method than convert cls object to dict
        :return: dict
        """
        return {
            "id": self.__id,
            "first_name": self.__first_name,
            "second_name": self.__second_name,
            "age": self.__age,
            "is_active": self.__is_active
        }

    @classmethod
    def from_dict(cls, obj_attr_dict: dict):
        return cls(
            obj_attr_dict['first_name'],
            obj_attr_dict['second_name'],
            obj_attr_dict['age'],
            obj_attr_dict['id'],
            obj_attr_dict['is_active']
        )

    def get_id(self) -> int:
        return self.__id

    def deactivate(self):
        self.__is_active = False

    def __str__(self):
        return f'{self.__id}_{self.__first_name} {self.__second_name}'

    def __repr__(self):
        return f'{self.__id}_{self.__first_name} {self.__second_name}'
