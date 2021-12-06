from multiprocessing import Process, Queue, Event
from socket import socket
from .msgutils import send_msg, default_encoding
import concurrent.futures as cf


class Sender(Process):

    def __init__(self, gen_queue: Queue, event: Event):
        super().__init__()
        self.gen_queue = gen_queue
        self.event = event

    def run(self):
        with cf.ThreadPoolExecutor(max_workers=10) as ex:
            thred_num = [i for i in range(1)]
            ex.map(self.send_func, thred_num)

    def send_func(self, _):
        """Method that connect to server and send primes"""
        with socket() as sock:
            sock.connect(('localhost', 12345))
            while True:
                prime = self.gen_queue.get()

                if prime == 0 or prime is None:
                    send_msg('End'.encode(default_encoding), sock)
                    self.event.set()
                    break

                if self.event.is_set():
                    break

                send_msg(f'{prime}'.encode(default_encoding), sock)
