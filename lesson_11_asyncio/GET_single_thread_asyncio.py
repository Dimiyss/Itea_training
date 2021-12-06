import requests
from time import time
from contextlib import contextmanager
import concurrent.futures as cf
import asyncio, aiohttp
from requests_futures import sessions

URL = 'http://httpbin.org/delay/1'
N_COUNT = 200

@contextmanager
def el_time(name_test):
    start = time()
    yield
    print(f'Time for {name_test} need: {time() - start}')


# # 1
# with el_time('Simple'):
#     for _ in range(N_COUNT):
#         requests.get(URL)
#
#
# # 2
# with el_time('Session'):
#     session = requests.Session()
#     for _ in range(N_COUNT):
#         session.get(URL)


# # 3
# with el_time('Threads'):
#     with cf.ThreadPoolExecutor() as ex:
#         for _ in range(N_COUNT):
#             ex.submit(requests.get, URL)


# 4
# with el_time('FuturesSession 2 workers'):
#     session = sessions.FuturesSession(max_workers=2)
#     futures = [session.get(URL) for _ in range(N_COUNT)]
#     res = [f.result() for f in futures]


# 5
with el_time(f'FuturesSession {N_COUNT} workers'):
    session = sessions.FuturesSession(max_workers=N_COUNT)
    futures = [session.get(URL) for _ in range(N_COUNT)]
    res = [f.result() for f in futures]


# 4
async def get(url):
    async with aiohttp.ClientSession() as s:
        async with s.get(url) as resp:
            await resp.read()

loop = asyncio.get_event_loop()
with el_time('ASYNCIO'):
    loop.run_until_complete(asyncio.gather(*[get(URL) for _ in range(N_COUNT)]))