import socket
from network_protocol import recv_msg, send_msg
from config import IP, PORT
# import main

sock = socket.socket()
sock.connect((IP, PORT))

data = recv_msg(sock)
reader_id = input(data)

send_msg(reader_id, sock)


