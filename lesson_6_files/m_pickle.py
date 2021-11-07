import pickle


class Reader:
    """
    Comment for class reader...
    """

    def __init__(self, name: str, surname: str, year: int, _id: int = None):
        self.__id = _id if _id is not None else int(id(self))
        self.__name = name
        self.__surname = surname
        self.__year = year

    def __str__(self):
        return f'{self.__id}) {self.__name} {self.__surname}, {self.__year}.'

    def get_id(self) -> int:
        return self.__id
#
#
# reader_1 = Reader('Tom', 'Berk', 30)

# with open('readers.db', 'ab') as f:
#     pickle.dump(reader_1, f)

reader_2 = None
with open('readers.db', 'rb') as f:
    reader_2 = pickle.load(f)

print(reader_2)