import socket
from config import DEFAULT_ENCODING, DEFAULT_PACK_SIZE, DEFAULT_HEADER_SIZE


def send_msg(msg: str, conn: socket, header_size: int = DEFAULT_HEADER_SIZE) -> bool:

    msg_size = f'{len(msg):{header_size}}'

    if conn.send(msg_size.encode(DEFAULT_ENCODING)) != header_size:
        print(f'ERROR: can\'t send size message')
        return False

    if conn.send(msg.encode(DEFAULT_ENCODING)) != len(msg):
        print(f'ERROR: can\'t send message')
        return False

    return True


def recv_msg(conn: socket,
             header_size: int = DEFAULT_HEADER_SIZE,
             size_pack: int = DEFAULT_PACK_SIZE):

    data = conn.recv(header_size)

    if not data or len(data) != header_size:
        print('ERROR: can\'t read size message')
        return False

    size_msg = int(data.decode(DEFAULT_ENCODING))
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

    return msg.decode(DEFAULT_ENCODING)
