from multiprocessing import Process, Queue, Event
from socket import socket
from .config import IP, PORT, MAX_QUEUE
from .thread_sercer import Receiver


class Server(Process):
    """Server process"""

    def __init__(self, queue: Queue, event_finish: Event):
        super().__init__()
        self.queue = queue
        self.socket = None
        self.event_finish = event_finish
        self.daemon = True

    def run(self):
        self.socket = self.start_server()
        while True:
            conn, _ = self.socket.accept()
            receiver = Receiver(conn, self.queue)
            receiver.start()

        self.queue.put(0)
        return None

    def start_server(self) -> socket:
        sock = socket()
        sock.bind((IP, PORT))
        sock.listen(MAX_QUEUE)

        return sock
