import socket
import time
import threading


def client_handler(conn: socket.socket):
    time.sleep(5)
    conn.send('Hello, client!'.encode())
    conn.close()


if __name__ == '__main__':
    sock = socket.socket()
    sock.bind(('', 12345))
    sock.listen(1)

    while True:
        conn, _ = sock.accept()
        client_thread = threading.Thread(target=client_handler, args=(conn,))
        client_thread.start()

