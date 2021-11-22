from socket import socket


class MySendProtocol:

    default_number_size = 4
    default_header_size = 10
    default_pack_size = 5
    default_encodings = '866'


    def send_msg(
            self,
            msg: bytes,
            conn: socket,
            message_num: int,
            header_size: int = default_header_size,
            message_size: int = default_number_size) -> bool:

        if message_num >= 10 ** message_size:
            print(f'ERROR: wrong message number: {message_num}, max number = {(10 ** message_size) - 1}')

        msg_num = f'{message_num:{message_size}}'
        # size of message
        msg_size = f'{len(msg):{header_size}}'

        # send header
        if conn.send(msg_size.encode()) != header_size:
            print(f'ERROR: can\'t send size message')
            return False

        # send data
        if conn.send(msg) != len(msg):
            print(f'ERROR: can\'t send size message')
            return False

        return True


    def recv_msg(conn: socket,
                 header_size: int = default_header_size,
                 size_pack: int = default_pack_size):
        data = conn.recv(header_size)
        if not data or len(data) != header_size:
            print('ERROR: can\'t read size message')
            return False

        size_msg = int(data.decode(default_encodings))
        msg = b''

        while True:
            if size_msg <= size_pack:
                pack = conn.recv(size_msg)
                if not pack:
                    return False

                msg += pack
                break

            pack = conn.recv(size_pack)
            if not pack:
                return False

            size_msg -= size_pack
            msg += pack

        return msg
