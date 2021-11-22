from network_protocol import send_msg, recv_msg
from config import MAX_ATTEMPT, IP, PORT, MAX_QUEUE
# from main import main_action
import socket


def send_attemp(msg, conn):
    attempt = 1
    send_result = False

    while attempt < MAX_ATTEMPT and not send_result:
        send_result = send_msg(msg, conn)
        attempt += 1

    return attempt


def auth_reader(conn):
    send_attemp("Enter your reader id", conn)

    reader_id = recv_msg(conn)
    print(reader_id)

    if not reader_id:
        send_attemp(2, conn)

        reader_list = recv_msg(conn)
        # main_action(2, reader_list)




sock = socket.socket()
sock.bind((IP, PORT))
sock.listen(MAX_QUEUE)

while True:
    conn, client_addr = sock.accept()

    reader_id = auth_reader(conn)

