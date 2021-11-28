from network_protocol import send_msg, recv_msg
from config import IP, PORT, MAX_QUEUE, NetworkMessage, ActionList
from DALibrary.library import Library
from DALibrary.units.reader import Reader
from DALibrary.units.book import Book
from DALibrary.storage.json_db import JsonDB
import socket

PATH = 'file_db/'


def start_server() -> socket:
    sock = socket.socket()
    sock.bind((IP, PORT))
    sock.listen(MAX_QUEUE)

    return sock


def created_book_from_file(lib) -> None:
    with open('.test_files/books.txt') as book_file:
        default_books = book_file.readlines()

        for book in default_books:
            lib.add_book(Book(book.split(';')[0],
                              book.split(';')[1],
                              book.split(';')[2],
                              book.split(';')[3])
                         )


def created_reader_from_file(lib) -> None:
    with open('.test_files/readers.txt') as reader_file:
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
    my_library = Library(connector_db, connector_db.load_books(), connector_db.load_readers())

    if not my_library.get_book_list():
        print('Init book load')
        created_book_from_file(my_library)

    if not my_library.get_reader_list():
        print('Init reader load')
        created_reader_from_file(my_library)

    return connector_db, my_library


def main_loop_server(client_conn: socket, my_library: Library):
    send_msg({'action': ActionList.OK.value, 'data': None}, client_conn)

    input_msq = recv_msg(client_conn)

    if not input_msq:
        client_conn.close()
        return False

    action = input_msq.get('action')
    ad_data = input_msq.get('data')

    while action != ActionList.END.value:

        server_msg: NetworkMessage = {'action': None, 'data': None}

        if action == ActionList.CREATE_BOOK.value:
            res = my_library.add_book(Book.from_dict(ad_data))
            server_msg['action'] = ActionList.OK.value
            server_msg['data'] = res

        if action == ActionList.CREATE_READER.value:
            res = my_library.add_reader(Reader.from_dict(ad_data))
            server_msg['action'] = ActionList.OK.value
            server_msg['data'] = res

        if action == ActionList.GIVE_BOOK.value:
            res = my_library.give_book(ad_data['book_id'], ad_data['reader_id'])
            server_msg['action'] = ActionList.OK.value
            server_msg['data'] = res

        if action == ActionList.RETURN_BOOK.value:
            res = my_library.return_book(ad_data['book_id'])
            server_msg['action'] = ActionList.OK.value
            server_msg['data'] = res

        if action == ActionList.PRINT_ALL_BOOK.value:
            res = [book.to_dict() for book in my_library.get_book_list()]
            server_msg['action'] = ActionList.OK.value
            server_msg['data'] = res

        if action == ActionList.PRINT_AVAILABLE_BOOK.value:
            res = [book.to_dict() for book in my_library.get_available_book_list()]
            server_msg['action'] = ActionList.OK.value
            server_msg['data'] = res

        if action == ActionList.PRINT_BUSY_BOOK.value:
            res = [book.to_dict() for book in my_library.get_busy_book_list()]
            server_msg['action'] = ActionList.OK.value
            server_msg['data'] = res

        if action == ActionList.SORTED_BOOK.value:
            res = [book.to_dict() for book in my_library.sorted_book(sort_key=ad_data['sort_key'],
                                                                     is_reverse=ad_data['revers'])]
            server_msg['action'] = ActionList.OK.value
            server_msg['data'] = res

        if action == ActionList.END.value:
            client_conn.close()
            return True

        send_msg(server_msg, client_conn)
        input_msq = recv_msg(client_conn)
        if not input_msq:
            client_conn.close()
            return False

        action = input_msq.get('action')
        ad_data = input_msq.get('data')


if __name__ == '__main__':
    connector, library = start_library_from_db(PATH)
    socket_server = start_server()

    while True:
        conn, client_addr = socket_server.accept()

        main_loop_server(conn, library)
