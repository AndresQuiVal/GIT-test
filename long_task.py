import asyncio

async def long_task(id, time):
    print(f"Task {id} started")
    await asyncio.sleep(time)
    print(f"Task {id} finished")

async def async_func():
    await asyncio.gather(
        long_task(1, 1),
        long_task(2, 2),
        long_task(3, 3)
    )

def run():
    asyncio.run(async_func())

if __name__ == '__main__':
    run()
