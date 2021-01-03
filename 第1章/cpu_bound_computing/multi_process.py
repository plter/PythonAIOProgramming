import asyncio
import concurrent.futures


def task():
    print("cpu bound task")
    pass


async def main():
    pool = concurrent.futures.ProcessPoolExecutor()
    await asyncio.get_running_loop().run_in_executor(pool, task)


if __name__ == '__main__':
    asyncio.run(main())
