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

    def __setstate__(self, state):
        # for k, v in state.items():

        self.__id = state['_Reader__id']
        self.__name = state['_Reader__name']
        self.__surname = state['_Reader__surname']
        self.__year = state['_Reader__year']

        print(f'Bang!!!')


reader_2 = None
with open('readers.db', 'rb') as f:
    reader_2 = pickle.load(f)