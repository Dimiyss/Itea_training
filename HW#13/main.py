from DALibrary.library import Library
from DALibrary.units import reader as reader_c, book as book_c
from DALibrary.utils.to_int import to_int
from DALibrary.storage.psycop_db import PsyCopgDB
from random import randint
from time import sleep

config = "dbname=postgres user=postgres password=pgpwd4habr host=localhost port=5432"

ACTION_LIST = """Please choose action:
                1 - create book;
                2 - create reader;
                3 - give book to reader;
                4 - return book;
                5 - print all book;
                6 - print available book;
                7 - print reader books list;
                8 - delete book list;
                9 - end program.
                """


def first_load_from_file():
    return Library()


def created_book_from_file(lib):
    global book_count_file
    with open('test_files/books.txt') as book_file_1:
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
    with open('test_files/readers.txt') as book_file_1:
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


def choise():
    while True:
        choise_user = to_int(input(ACTION_LIST))

        return choise_user


def main_loop():
    connector = PsyCopgDB(config)
    my_library = Library(connector)
    while True:
        action = choise()
        if action == 1:
            title = input('Pls, enter book title: ')
            author = input('Pls, enter book author: ')
            published_year = to_int(input('Pls, enter book published year: '))
            genre = input('Pls, enter book genre: ')
            my_library.add_book(book_c.Book(title, author, published_year, genre))
        elif action == 2:
            first_name = input('Pls, enter reader first name: ')
            second_name = input('Pls, enter reader second name: ')
            age = to_int(input('Pls, enter reader age: '))
            my_library.add_reader(reader_c.Reader(first_name, second_name, age))
        elif action == 3:
            book_id = to_int(input('Pls, enter book_id that will given to reader'))
            reader_id = to_int(input('Pls, enter reader_id'))
            print(my_library.give_book(book_id, reader_id))
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
            reader_id = to_int(input('Pls, enter reader_id which book will show'))
            print('************************************************************************')
            print(my_library.get_reader_books(reader_id))
            print('************************************************************************')
            sleep(2)
        elif action == 8:
            book_id = to_int(input('Pls, enter book_id that will be delete from library: '))
            print('************************************************************************')
            print(my_library.delete_book(book_id))
            print('************************************************************************')
            sleep(1)
        elif action == 9:
            return None
        else:
            print('Wrong please repeat.....')


if __name__ == '__main__':

    main_loop()
