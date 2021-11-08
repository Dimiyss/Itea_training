import library as library_c
import utils.book as book_c
import utils.reader as reader_c
from json_db import JsonDB
from random import randint
from time import sleep

book_count_file = 0
reader_count_file = 0
const_path = './file_db/'


def first_load_from_file():
    return library_c.Library()


def created_book_from_file(lib):
    global book_count_file
    with open('/test_files/books.txt') as book_file_1:
        default_book = book_file_1.readlines()
        if book_count_file > len(default_book):
            book_count_file = 0
        lib.add_book(book_c.Book(default_book[book_count_file].split(';')[0],
                     default_book[book_count_file].split(';')[1],
                     default_book[book_count_file].split(';')[2],
                     default_book[book_count_file].split(';')[3])
                     )
    book_count_file += 1


def created_reader_from_file(lib):
    global reader_count_file
    with open('../test_files/readers.txt') as book_file_1:
        default_reader = book_file_1.readlines()
        if reader_count_file > len(default_reader):
            reader_count_file = 0
        lib.add_reader(
            reader_c.Reader(
                default_reader[reader_count_file].split(';')[0],
                default_reader[reader_count_file].split(';')[1]
            )
        )
    reader_count_file += 1


if __name__ == '__main__':
    connector = JsonDB(const_path)
    print('Create library type:')
    try:
        action_1 = int(input(
            """Please choose creation type:
                0 - create library from db;
                1 - create empty library.
                """)
        )
    except ValueError:
        print('Wrong choice')
    if action_1 == 0:
        my_library = library_c.Library(JsonDB.load_books(), JsonDB.load_readers())
    else:
        my_library = first_load_from_file()

    while True:
        print('Current library:')
        print(my_library)
        try:
            action = int(input(
                """Please choose action:
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
                               )
                         )
        except ValueError:
            print('Wrong choice')
            continue
        if action == 1:
            created_book_from_file(my_library)
            connector.save_books(my_library.get_book_list())
        elif action == 2:
            created_reader_from_file(my_library)
            connector.save_readers(my_library.get_reader_list())
        elif action == 3:
            try:
                book_id = int(input('Pls, enter book_id that will given to reader'))
                reader_id = int(input('Pls, enter reader_id'))
            except ValueError:
                print('Wrong choice, to be use default 1, 1')
                book_id = 1
                reader_id = 1
            print(my_library.give_book(book_id, reader_id))
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
