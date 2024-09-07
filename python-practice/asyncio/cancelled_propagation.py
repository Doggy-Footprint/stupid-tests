import asyncio

async def coro(coro_num: int, sleep: int = 3):
    print(f'coro start: {coro_num}')
    await asyncio.sleep(sleep)
    print(f'coro end: {coro_num}')


async def coro_attr_exc():
    print('exception in 3 seconds!')
    await asyncio.sleep(3)
    raise AttributeError()

async def inner():
    # try:
        async with asyncio.TaskGroup() as tg:
            tg.create_task(coro(1, 1))
            tg.create_task(coro(2, 5))
            tg.create_task(coro(3, 100))
            tg.create_task(coro_attr_exc())
        print('tg is finished')
    # except ExceptionGroup as e:
    #     print('ExceptionGroup in tg', e)
    #     raise e

async def outer():
    await asyncio.sleep(0.5)
    async with asyncio.TaskGroup() as outer_tg:
        outer_tg.create_task(coro(4,10))
        outer_tg.create_task(inner())
    print('tg_outer finished')

asyncio.run(outer())