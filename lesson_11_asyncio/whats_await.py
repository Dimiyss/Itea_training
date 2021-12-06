from time import time, sleep
import asyncio

async def task_1():
    print(f'Task #1 starting {time()}')
    await asyncio.sleep(2)
    print(f'Task #1 finished {time()}')


async def task_2():
    print(f'Task #2 starting {time()}')
    await asyncio.sleep(1)
    print(f'Task #2 finished {time()}')


async def task_3():
    print(f'Task #3 starting {time()}')
    await asyncio.sleep(2.5)
    print(f'Task #3 finished {time()}')