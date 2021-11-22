import time
from threading import Thread
from concurrent.futures import ThreadPoolExecutor

counter = 0


def thread_func(n):
    global counter

    for i in range(*n):
        counter += 1


with ThreadPoolExecutor(max_workers=128) as ex:
    for i in range(10000):
        ex.submit(thread_func, (10000, ))

print(counter)