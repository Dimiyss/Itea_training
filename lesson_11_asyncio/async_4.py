import asyncio
import aiohttp
import time
from concurrent.futures import FIRST_COMPLETED
import requests


async def fetch_ip(session, param, service):
    start = time.time()
    print(f'Fetching IP from {service}')

    async with session.get(service) as r:
        j_r = await r.json()
    ip = j_r[param]

    return f'{service} finished with result: {ip}, took: {time.time() - start}'


async def create_tasks():
    async with aiohttp.ClientSession() as session:
        tasks = [
            fetch_ip(session, 'ip', 'https://api.ipify.org?format=json'),
            fetch_ip(session, 'query', 'http://ip-api.com/json'),
        ]

        done, pending = await asyncio.wait(tasks, return_when=FIRST_COMPLETED)

        print(f'PENDING: {pending}')
        print(f'DONE: {done}')

        print(done.pop().result())

        for future in pending:
            future.cancel()


loop = asyncio.get_event_loop()
loop.run_until_complete(create_tasks())
