import json

from ..DALibrary.library import Library
from ..DALibrary.units.reader import Reader
from ..DALibrary.units.book import Book
from ..DALibrary.storage.json_db import JsonDB
from random import randint
from time import sleep

book_count_file = 0
reader_count_file = 0
const_path = 'file_db/'

ACTION_LIST = """Please choose action:
                1 - create book;
                2 - create reader;
                3 - give book to reader;
                4 - return book;
                5 - print all book;
                6 - print available book;
                7 - print busy book;
                8 - sorted book list;
                9 - end program.
                """


def created_book_from_file(lib) -> None:

    with open('..test_files/books.txt') as book_file:
        default_books = book_file.readlines()

        for book in default_books:
            lib.add_book(Book(book.split(';')[0],
                         book.split(';')[1],
                         book.split(';')[2],
                         book.split(';')[3])
                         )


def created_reader_from_file(lib) -> None:

    with open('..test_files/readers.txt') as reader_file:
        default_reader = reader_file.readlines()

        for reader in default_reader:
            lib.add_reader(
                Reader(
                    reader.split(';')[0],
                    reader.split(';')[1]
                )
            )

def start_library_from_db(path) -> tuple:

    connector_db = JsonDB(path)
    my_library = Library(connector_db, connector_db.load_books(), connector.load_readers())

    if not my_library.get_book_list():
        print('Init book load')
        created_book_from_file(my_library)

    if not my_library.get_reader_list():
        print('Init reader load')
        created_reader_from_file(my_library)

    return connector_db, my_library


def main_action(action: int, data, library: Library):
    #while True:
        # print('Current library:')
        # print(my_library)
        # try:
        #     action = int(input(ACTION_LIST))
        # except ValueError:
        #     print('Wrong choice')
        #     continue
    if action == 1:
        library.add_book(Book.from_dict(json.loads(data)))
    if action == 2:
        library.add_reader(Reader.from_dict(json.loads(data)))

    if action == 3:
        # try:
        #     book_id = int(input('Pls, enter book_id that will given to reader'))
        #     reader_id = int(input('Pls, enter reader_id'))
        # except ValueError:
        #     print('Wrong choice, to be use default 1, 1')
        #     book_id = 1
        #     reader_id = 1
        library.give_book(book_id, reader_id))
        connector.save_books(my_library.get_book_list())
        sleep(2)
    elif action == 4:
        try:
            book_id = int(input('Pls, enter book_id that will be return to library'))
        except ValueError:
            print('Wrong choice, to be use random(0-10)')
            book_id = randint(1, 10)
        print('************************************************************************')
        print(my_library.return_book(book_id))
        print('************************************************************************')
        connector.save_books(my_library.get_book_list())
        sleep(2)
    elif action == 5:
        print('************************************************************************')
        print(my_library.get_book_list())
        print('************************************************************************')
        sleep(2)
    elif action == 6:
        print('************************************************************************')
        print(my_library.get_available_book_list())
        print('************************************************************************')
        sleep(2)
    elif action == 7:
        print('************************************************************************')
        print(my_library.get_busy_book_list())
        print('************************************************************************')
        sleep(2)
    elif action == 8:
        try:
            sort_key_id = int(input('Enter sort key: 1-title, 2-publish year, 3-author(default)'))
            revers_id = int(input('Sort way: 1-ASC, 2-DESC'))
        except ValueError:
            print('Wrong choice, to be use author and ASC)')
            sort_key_id = 3
            revers_id = 1
        if sort_key_id == 1:
            sort_key = 'title'
        elif sort_key_id == 2:
            sort_key = 'published_date'
        else:
            sort_key = 'author'
        if revers_id == 2:
            revers = True
        else:
            revers = False
        print('************************************************************************')
        print(my_library.sorted_book(sort_key=sort_key, is_reverse=revers))
        print('************************************************************************')
        sleep(2)
    else:
        break


if __name__ == '__main__':
    connector, library = start_library_from_db(const_path)
    #print('Create library type:')

    # my_library = Library(connector.load_books(), connector.load_readers())
    #
    # if not my_library.get_book_list():
    #     print('Init book load')
    #     created_book_from_file(my_library)
    #
    # if not my_library.get_reader_list():
    #     print('Init reader load')
    #     created_reader_from_file(my_library)
    # try:
    #     action_1 = int(input(
    #         """Please choose creation type:
    #             0 - create library from db;
    #             1 - create empty library.
    #             """)
    #     )
    # except ValueError:
    #     print('Wrong choice')
    # if action_1 == 0:
    #     my_library = library_c.Library(connector.load_books(), connector.load_readers())
    # else:
    #     my_library = first_load_from_file()
    # def main_acion(action):
    #     while True:
    #         # print('Current library:')
    #         # print(my_library)
    #         # try:
    #         #     action = int(input(ACTION_LIST))
    #         # except ValueError:
    #         #     print('Wrong choice')
    #         #     continue
    #         if action == 1:
    #             #created_book_from_file(my_library)
    #             send_msg = ''
    #             connector.save_books(my_library.get_book_list())
    #         elif action == 2:
    #             created_reader_from_file(my_library)
    #             connector.save_readers(my_library.get_reader_list())
    #         elif action == 3:
    #             try:
    #                 book_id = int(input('Pls, enter book_id that will given to reader'))
    #                 reader_id = int(input('Pls, enter reader_id'))
    #             except ValueError:
    #                 print('Wrong choice, to be use default 1, 1')
    #                 book_id = 1
    #                 reader_id = 1
    #             print(my_library.give_book(book_id, reader_id))
    #             connector.save_books(my_library.get_book_list())
    #             sleep(2)
    #         elif action == 4:
    #             try:
    #                 book_id = int(input('Pls, enter book_id that will be return to library'))
    #             except ValueError:
    #                 print('Wrong choice, to be use random(0-10)')
    #                 book_id = randint(1, 10)
    #             print('************************************************************************')
    #             print(my_library.return_book(book_id))
    #             print('************************************************************************')
    #             connector.save_books(my_library.get_book_list())
    #             sleep(2)
    #         elif action == 5:
    #             print('************************************************************************')
    #             print(my_library.get_book_list())
    #             print('************************************************************************')
    #             sleep(2)
    #         elif action == 6:
    #             print('************************************************************************')
    #             print(my_library.get_available_book_list())
    #             print('************************************************************************')
    #             sleep(2)
    #         elif action == 7:
    #             print('************************************************************************')
    #             print(my_library.get_busy_book_list())
    #             print('************************************************************************')
    #             sleep(2)
    #         elif action == 8:
    #             try:
    #                 sort_key_id = int(input('Enter sort key: 1-title, 2-publish year, 3-author(default)'))
    #                 revers_id = int(input('Sort way: 1-ASC, 2-DESC'))
    #             except ValueError:
    #                 print('Wrong choice, to be use author and ASC)')
    #                 sort_key_id = 3
    #                 revers_id = 1
    #             if sort_key_id == 1:
    #                 sort_key = 'title'
    #             elif sort_key_id == 2:
    #                 sort_key = 'published_date'
    #             else:
    #                 sort_key = 'author'
    #             if revers_id == 2:
    #                 revers = True
    #             else:
    #                 revers = False
    #             print('************************************************************************')
    #             print(my_library.sorted_book(sort_key=sort_key, is_reverse=revers))
    #             print('************************************************************************')
    #             sleep(2)
    #         else:
    #             break
