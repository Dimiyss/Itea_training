import time
from threading import Thread
from concurrent.futures import ThreadPoolExecutor

counter = 0


def thread_func(n):
    global counter

    for i in range(n):
        counter += 1

threads = []
for i in range(10000):
    thread = Thread(target=thread_func, args=(10000,))
    threads.append(thread)

# start threads
for th in threads:
    th.start()

# wait finish threads
for th in threads:
    th.join()

print(counter)