import time
from threading import Thread, Lock, RLock
from concurrent.futures import ThreadPoolExecutor

# counter = 0
# lock = Lock()
#
#
# def thread_func(n):
#     global counter
#
#     for i in range(*n):
#         lock.acquire()
#         counter += 1
#         lock.release()

# for i in range(10000):
#     thread_func(10000)
#
# print(counter)
# 100 000 000


# with ThreadPoolExecutor(max_workers=128) as ex:
#     for i in range(10000):
#         ex.submit(thread_func, (10000, ))

# without Lock
# 94389347
# 72370003
# 93045303

# with Lock
#
# print(counter)


class FakeDB:
    def __init__(self):
        self.value = 0
        self._lock = RLock()

    def inc(self, name):
        print(f'Thread #{name} starting inc')

        # self._lock.acquire()
        # local_copy = self.value
        # local_copy += 1
        #
        # time.sleep(0.1)
        # self.value = local_copy
        # self._lock.release()

        with self._lock:
            local_copy = self.value
            local_copy += 1

            time.sleep(0.1)
            self.value = local_copy

        print(f'Thread #{name} finished inc')

db = FakeDB()
with ThreadPoolExecutor(max_workers=2) as ex:
    for i in range(2):
        ex.submit(db.inc, i)

print(db.value)