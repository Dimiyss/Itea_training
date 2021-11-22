import time
import socket


with socket.socket() as sock:
    sock.connect(('localhost', 12345))

    start = time.time()
    msg = sock.recv(20)
    print(msg.decode())
    print(f'time = {time.time() - start}')