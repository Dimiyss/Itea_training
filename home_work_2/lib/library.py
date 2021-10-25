import home_work_2.lib.book as b
import home_work_2.lib.reader as r


class Library:
    def __init__(self, book_list, reader_list):
        self.book_list = book_list
        self.reader_list = reader_list

    def add_book(self, *args):
        book = b.Book(*args)
        self.book_list.append(book)

    def add_reader(self, *args):
        reader = r.Reader(*args)
        self.reader_list.append(reader)

    def delete_book(self, book):
        self.book_list.remove(book)
        book.__del__()

    def give_book(self, book_id, reader_id):
        for reader in self.reader_list:
            if reader.id == reader_id:
                break
        else:
            print(f'Reader with id {reader_id} is not exists')
            return 'Done'
        for book in self.book_list:
            if book.id == book_id and book.current_place == 0:
                book.set_current_place(reader_id)
                break
            elif book.id == book_id and book.current_place != 0:
                print(f'{book} is not available')
                break
            else:
                continue
        else:
            print(f'Book with id {book_id} is not found')

    def return_book(self, book_id):
        for book in self.book_list:
            if book.id == book_id:
                book.set_current_place(0)
                break

    def all_book_print(self):
        print(f'All book in library:\n {self.book_list}')

    def all_available_print(self):
        available_book = []
        for book in self.book_list:
            if book.current_place == 0:
                available_book.append(book)
            else:
                continue
        if available_book:
            print(f'Available book in library:\n {available_book}.')
        else:
            print('Sorry, no available book.')

    def all_busy_print(self):
        busy_book = []
        for book in self.book_list:
            if book.current_place != 0:
                busy_book.append(book)
            else:
                continue
        if busy_book:
            print(f'Book in readers now:\n {busy_book}')
        else:
            print('All book in library.')

    def sorted_book(self, sort_key, is_reverse=False):
        return sorted(self.book_list, key=lambda x: x.__getattribute__(sort_key), reverse=is_reverse)

    def __repr__(self):
        return f'All books in lib: {self.book_list}\nAll readers: {self.reader_list}'

    def __str__(self):
        return f'All books in lib: {self.book_list}\nAll readers: {self.reader_list}'
