import asyncio


# async def callee():
#     print('Hello')
#
#
# async def caller():
#     await callee()
#     # asyncio.create_task(callee())
#     print('World')
#
#
# asyncio.run(caller())


async def callee():
    return 'Hello'


async def caller():
    # loop = asyncio.get_event_loop()
    # future = loop.create_task(callee())
    # # future = asyncio.ensure_future(callee())
    future = asyncio.create_task(callee())
    # res = await future

    # while not future.done():
    #     print('wait...')
    #     await asyncio.sleep(0.1)

    future.add_done_callback(lambda res: print(res.result() + ' World'))
    print('Finishing...')


asyncio.run(caller())
