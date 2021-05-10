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


def print_msg(msg):
    print(f"HOLA: {msg}")

def run():
    asyncio.run(async_func())
    print_msg("MUNDO")

if __name__ == '__main__':
    run()
