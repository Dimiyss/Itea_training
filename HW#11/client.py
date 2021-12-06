from client_units.generate_process import PrimeGenerator
from client_units.transmiter import Sender
from multiprocessing import Manager, Event
from time import time, sleep


def start_client():
    sleep(0.1)
    start_time = time()

    m = Manager()
    client_queue = m.Queue()
    event = Event()
    sender1 = Sender(client_queue, event)
    sender1.start()

    generator = PrimeGenerator(client_queue)
    generator.start()

    sender2 = Sender(client_queue, event)
    sender2.start()

    generator.join()
    #print(f'generator end {time() - start_time}')
    sender1.join()
    sender2.join()

    print(f'Client end {time() - start_time}')

if __name__ == '__main__':
    #start_time = time()
    start_client()
    #sem = Semaphore(2)
    #print(f' Transceiver work time = {time() - start_time}')
