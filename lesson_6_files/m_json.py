import json

# reader = {
#     "name": "Tom",
#     "age": 30
# }

# print(reader)
#
# json_obj = json.dumps(reader)
#
# print(type(json_obj))
#
# new_reader = json.loads(json_obj)
# print(type(new_reader))
# print(f'name = {new_reader["name"]}')

# with open('reader.json', 'w') as f:
#     json.dump(reader, f)
#
#
# with open('reader.json', 'r') as f:
#     new_reader = json.load(f)
#     print(type(new_reader))


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

    def to_dict(self):
        return {
            "name": self.__name,
            "surname": self.__surname,
            "year": self.__year,
            "id": self.__id,
        }

    @classmethod
    def reader_from_dict(cls, dict_obj):
        return cls(dict_obj['name'], dict_obj['surname'], dict_obj['year'], dict_obj['id'])


# reader_1 = Reader('Tom', 'Berk', 30)
# reader_2 = Reader('Tom', 'Berk', 20)
#
# with open('reader.json', 'a') as f:
#     obj_str_1 = json.dumps(reader_1.to_dict())
#     f.write(obj_str_1 + '\n')
#
#     obj_str_2 = json.dumps(reader_2.to_dict())
#     f.write(obj_str_2 + '\n')

readers = []
with open('reader.json', 'r') as f:
    for line in f:
        readers.append(Reader.reader_from_dict(json.loads(line)))

for reader in readers:
    print(reader)