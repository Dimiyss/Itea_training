from time import time, sleep
import asyncio

start = time()
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


asyncio.run(task_1())
# loop = asyncio.get_event_loop()
#
# tasks = [
#     loop.create_task(task_1()),
#     loop.create_task(task_2()),
#     loop.create_task(task_3()),
# ]
#
# qwerty = asyncio.wait(tasks)
# loop.run_until_complete(qwerty)
# print(f'time elapsed = {time() - start}')