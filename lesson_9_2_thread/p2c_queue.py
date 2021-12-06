from random import randint
import concurrent.futures as cf
from queue import Queue
from time import time_ns, sleep
from threading import Event


setM = 0
getM = 0


def producer(pipeline: Queue, event_finish: Event):
    global setM
    while not event_finish.is_set():
        msg = randint(1, 100)

        pipeline.put(msg)
        print(f'Producer got message: {msg}')
        setM += 1


def consumer(pipeline: Queue, event_finish: Event):
    global getM
    msg = None

    # 1 or 1 = 1
    # 0 or 1 = 1
    # 1 or 0 = 1
    # 0 or 0 = 0

    while not event_finish.is_set() or not pipeline.empty():
        msg = pipeline.get()
        getM += 1
        print(f'Consumer read message: {msg}')


if __name__ == '__main__':
    pipeline = Queue()
    event_finish = Event()

    start = time_ns()
    with cf.ThreadPoolExecutor(max_workers=2) as ex:
        ex.submit(producer, pipeline, event_finish)
        ex.submit(consumer, pipeline, event_finish)

        sleep(1)
        event_finish.set()

    print(f'time = {time_ns() - start} nsec.')

    print(f'setM = {setM}')
    print(f'getM = {getM}')

# 36 32 63 79 29 35 81 94 95 45
# 36 32 63 79 29 35 81 94 95 45


# time one msg = 6 999 200 nsec.
# time queue msg = 5 996 900 nsec.
# time = 3 999 000 nsec.