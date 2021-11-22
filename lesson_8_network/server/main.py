import socket
from msgutils import send_msg, recv_msg, default_encoding


sock = socket.socket()
sock.bind(('', 1234))
sock.listen(1)

while True:
    conn, client_addr = sock.accept()
    print(f'Accept new connection: {client_addr}')

    data = recv_msg(conn)
    print(data.decode(default_encoding))

    send_msg('Thanks'.encode(default_encoding), conn)
    conn.close()