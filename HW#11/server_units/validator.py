from multiprocessing import Process, Queue, Semaphore, Event
from .check_prime import is_prime


class Validator(Process):
    """Class that check is number prime"""

    def __init__(self, queue: Queue, queue_dest: Queue, event: Event, event_for_writer: Event, proc_num):
        super().__init__()
        self.queue_recv = queue
        self.queue_dest = queue_dest
        self.event = event
        self.event_for_writer = event_for_writer
        self.proc_num = proc_num

    def run(self):

        num = 1

        # while not self.event.is_set() or not self.queue_recv.empty():
        while num != 0:

            # self.semaphore.acquire()
            num = self.queue_recv.get()
            # self.semaphore.release()
            #print(num)

            is_num_prime = is_prime(num)

            if is_num_prime:
                #print(f'Put in destanation queue {num}')
                self.queue_dest.put(num)

            # print(f'Process {self.proc_num} queue empty - {self.queue_recv.empty()}')
            #print(f'Process {num} end {self.event.is_set()}')

        print('Validator ended')
        self.event_for_writer.set()
        self.queue_dest.put(0)
        return None

