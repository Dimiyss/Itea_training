import time
from concurrent.futures import ThreadPoolExecutor


def thread_func(_):
    print(f'function # starting')
    time.sleep(1)
    print(f'function # finished')


with ThreadPoolExecutor(max_workers=10) as ex:
    ex.map(thread_func, range(10))

print('finished')

