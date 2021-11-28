import socket
from network_protocol import recv_msg, send_msg
from config import IP, PORT
from action_list_enum import NetworkMessage, ActionList

ACTION_LIST = """Please choose action:
                1 - create book;
                2 - create reader;
                3 - give book to reader;
                4 - return book;
                5 - print all book;
                6 - print available book;
                7 - print busy book;
                8 - sorted book list;
                9 - end program.\n
                """


def input_numeric(msg: str) -> int:
    while True:
        inp = input(msg)
        if inp.isnumeric():
            return int(inp)
        else:
            input('Press Enter to continue...')


def connect_to_server() -> socket:
    sock_ser = socket.socket()
    sock_ser.connect((IP, PORT))

    return sock_ser


def input_action() -> int:
    _choise = input_numeric(ACTION_LIST)

    if _choise < 0 or _choise > 9:
        input('Press Enter to continue...')
    else:
        return _choise


def main_action_loop(conn: socket) -> bool:
    print('Start main_action_loop')
    serv_msg = recv_msg(conn)
    if not serv_msg:
        return False

    print(serv_msg.get('action'))
    server_action = serv_msg.get('action')

    while True and server_action == ActionList.OK.value and conn:
        action = input_action()
        client_msg: NetworkMessage = {'action': None, 'data': None}
        aditional_data: dict = {}

        if action == 1:
            aditional_data['title'] = input('Enter the title of the book: ')
            aditional_data['author'] = input('Enter the author of the book: ')
            aditional_data['published_date'] = input_numeric('Enter the published year of the book: ')
            aditional_data['genre'] = input('Enter the genre of the book: ')
            aditional_data['id'] = None
            aditional_data['current_place'] = 0
            client_msg['action'] = ActionList.CREATE_BOOK.value
            client_msg['data'] = aditional_data

        if action == 2:
            aditional_data['first_name'] = input('Enter the First Name of the reader: ')
            aditional_data['second_name'] = input('Enter the First Name of the reader: ')
            aditional_data['id'] = None
            aditional_data['is_active'] = True
            client_msg['action'] = ActionList.CREATE_READER.value
            client_msg['data'] = aditional_data

        if action == 3:
            aditional_data['book_id'] = input_numeric('Pls, enter book_id that will given to reader')
            aditional_data['reader_id'] = input_numeric('Pls, enter reader_id')
            client_msg['action'] = ActionList.GIVE_BOOK.value
            client_msg['data'] = aditional_data

        if action == 4:
            aditional_data['book_id'] = input_numeric('Pls, enter book_id that will be return to library')
            client_msg['action'] = ActionList.RETURN_BOOK.value
            client_msg['data'] = aditional_data

        if action == 5:
            client_msg['action'] = ActionList.PRINT_ALL_BOOK.value

        if action == 6:
            client_msg['action'] = ActionList.PRINT_AVAILABLE_BOOK.value

        if action == 7:
            client_msg['action'] = ActionList.PRINT_BUSY_BOOK.value

        if action == 8:
            sort_key_id = input_numeric('Enter sort key: 1-title, 2-publish year, 3-author')
            revers_id = input_numeric('Sort way: 1-ASC, 2-DESC')

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

            aditional_data['sort_key'] = sort_key
            aditional_data['revers'] = revers
            client_msg['action'] = ActionList.SORTED_BOOK.value
            client_msg['data'] = aditional_data

        if action == 9:
            client_msg['action'] = ActionList.END.value
            send_msg(client_msg, conn)
            conn.close()
            return True

        send_msg(client_msg, conn)
        server_msg: NetworkMessage = recv_msg(conn)

        if server_msg.get('data'):
            print(server_msg.get('data'))

        server_action = server_msg.get('action')


if __name__ == '__main__':
    socket = connect_to_server()

    main_action_loop(socket)
