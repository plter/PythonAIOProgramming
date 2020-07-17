import asyncio
import concurrent.futures

from numba import jit
import time


# 一种计算圆周率算法
@jit
def compute_pi():
    count = 100000
    part = 1.0 / count
    inside = 0.0
    for i in range(1, count):
        for j in range(1, count):
            x = part * i
            y = part * j
            if x * x + y * y <= 1:
                inside += 1
    pi = inside / (count * count) * 4
    return pi


async def print_pi(pool):
    print(f"[{time.strftime('%X')}] Started to compute PI")
    # 将CPU密集型代码运行在进程池中
    pi = await asyncio.get_running_loop().run_in_executor(pool, compute_pi)
    print(f"[{time.strftime('%X')}] {pi}")


async def task():
    for i in range(5):
        print(f"[{time.strftime('%X')}] Step {i}")
        await asyncio.sleep(1)


async def main():
    # 声明进程池，进程池对象只需要声明一次，可在多处使用
    pool = concurrent.futures.ProcessPoolExecutor()

    await asyncio.gather(
        print_pi(pool),
        task()
    )


if __name__ == '__main__':
    asyncio.run(main())
