from threading import Thread, Event
import sys
from .msgutils import send_msg, recv_msg, default_encoding
from multiprocessing import Queue


class Receiver(Thread):

    def __init__(self, connection, queue: Queue):
        super().__init__(),
        self.connection = connection
        self.queue = queue
        #self.event = event

    def run(self):
        while self.connection:
            msg_raw = recv_msg(self.connection)
            if not msg_raw:
                print(f'not msg_raw = {msg_raw}')
                continue

            msg = msg_raw.decode(default_encoding)

            if msg == 'End':
                #self.event.set()
                self.queue.put(0)
                #
                sys.exit(0)

            #print(msg)
            if msg and msg != 'End':
                self.queue.put(int(msg))

        #print('return None')
        #self.event = 0
        self.queue.put(int(0))

        return None


