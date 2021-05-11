import asyncio
import time

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


def get_total_time(start_time):
    """
    Calculates the total time that it took to execute the script
    """
    return time.time() - start_time

def print_finished(msg):
    print(f"FINISHED, TIME: {time.time()}, MESSAGE: {msg}")

def run():
    start_time = time.time()
    asyncio.run(async_func())
    print_finished("tasks completed")
    print("Total time spent on executing the script: {}".format(get_total_time(start_time)))
if __name__ == '__main__':
    run()
