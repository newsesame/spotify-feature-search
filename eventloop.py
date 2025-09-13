import asyncio
import time


async def taskX():
    await asyncio.sleep(4)
    print("task0 Done")
async def task(id):
    time.sleep(1)
    print("task", id, " Done")

async def main():
    task0 = asyncio.create_task(taskX())
    task1 = asyncio.create_task(task(1))
    task2 = asyncio.create_task(task(2))
    task3 = asyncio.create_task(task(3))
    
    print("Main Task Started")
    await task1
    print("Main Task Finished")

if __name__ == "__main__":
    asyncio.run(main())