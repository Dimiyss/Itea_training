from random import randint
import concurrent.futures as cf
from time import time_ns, sleep

from multiprocessing import Manager, Queue, Event, Lock, RLock, Semaphore
from multiprocessing import Pipe


setM = 0
getM = 0


def producer(pipeline: Queue, event_finish: Event):
    global setM
    while not event_finish.is_set():
        msg = randint(1, 100)

        pipeline.put(msg)
        print(f'Producer got message: {msg}')
        setM += 1

    print(f'setM = {setM}')


def consumer(pipeline: Queue, event_finish: Event):
    global getM

    while not event_finish.is_set() or not pipeline.empty():
        msg = pipeline.get()
        getM += 1
        print(f'Consumer read message: {msg}')

    print(f'getM = {getM}')


if __name__ == '__main__':
    m = Manager()
    pipeline = m.Queue()
    event_finish = m.Event()

    start = time_ns()
    with cf.ProcessPoolExecutor(max_workers=2) as ex:
        ex.submit(producer, pipeline, event_finish)
        ex.submit(consumer, pipeline, event_finish)

        sleep(1)
        event_finish.set()

    print(f'time = {time_ns() - start} nsec.')

    print(f'setM = {setM}')
    print(f'getM = {getM}')