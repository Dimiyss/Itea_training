from socket import socket

default_header_sie = 10
default_pack_size = 5  #4096
default_encodings = '866'


def send_msg(msg: bytes, conn: socket, header_size: int = default_header_sie) -> bool:
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
             header_size: int = default_header_sie,
             size_pack: int = default_pack_size):
    data = conn.recv(header_size)
    if not data or len(data) != header_size:
        print('ERROR: can\'t read size message')
        return False

    size_msg = int(data.decode(default_encodings))
    msg = b''

    while True:
        if size_msg <=size_pack:
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
