import lib.library as library_c
from random import randint


book_count_file = 0
reader_count_file = 0


def first_load_from_file():
    book_list = []
    reader_list = []
    return library_c.Library(book_list, reader_list)


def created_book_from_file(lib):
    global book_count_file
    with open('test_files/books.txt') as book_file_1:
        default_book = book_file_1.readlines()
        if book_count_file > len(default_book):
            book_count_file = 0
        lib.add_book(default_book[book_count_file].split(';')[0],
                     default_book[book_count_file].split(';')[1],
                     default_book[book_count_file].split(';')[2],
                     default_book[book_count_file].split(';')[3]
                     )
    book_count_file += 1


def created_reader_from_file(lib):
    global reader_count_file
    with open('test_files/readers.txt') as book_file_1:
        default_reader = book_file_1.readlines()
        if reader_count_file > len(default_reader):
            reader_count_file = 0
        lib.add_reader(default_reader[reader_count_file].split(';')[0], default_reader[reader_count_file].split(';')[1])
    reader_count_file += 1


if __name__ == '__main__':
    my_library = first_load_from_file()

    while True:
        print('Current library:')
        print(my_library)
        try:
            action = int(input(
                """Please choose action:
                1 - create book;
                2 - create reader;
                3 - give book to reade;
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
        elif action == 2:
            created_reader_from_file(my_library)
        elif action == 3:
            print(f'All books: {my_library.book_list}')
            print(f'All readers: {my_library.reader_list}')
            try:
                book_id = int(input('Pls, enter book_id that will given to reader'))
                reader_id = int(input('Pls, enter reader_id'))
            except ValueError:
                print('Wrong choice, to be use default 1, 1')
                book_id = 1
                reader_id = 1
            my_library.give_book(book_id, reader_id)
        elif action == 4:
            try:
                book_id = int(input('Pls, enter book_id that will be return to library'))
            except ValueError:
                print('Wrong choice, to be use random(0-10)')
                book_id = randint(1, 10)
            my_library.return_book(book_id)
        elif action == 5:
            my_library.all_book_print()
        elif action == 6:
            my_library.all_available_print()
        elif action == 7:
            my_library.all_busy_print()
        elif action == 8:
            try:
                sort_key_id = int(input('Enter sort key: 1-name, 2-publish year, 3-author(default)'))
                revers_id = int(input('Sort way: 1-ASC, 2-DESC'))
            except ValueError:
                print('Wrong choice, to be use author and ASC)')
                sort_key_id = 3
                revers_id = 1
            if sort_key_id == 1:
                sort_key = 'name'
            elif sort_key_id == 2:
                sort_key = 'published_date'
            else:
                sort_key = 'author'
            if revers_id == 2:
                revers = True
            else:
                revers = False
            print(my_library.sorted_book(sort_key=sort_key, is_reverse=revers))
        else:
            break
