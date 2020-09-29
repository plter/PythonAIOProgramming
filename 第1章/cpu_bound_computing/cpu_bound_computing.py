"""
第1章/cpu_bound_computing.py
"""

import asyncio
import concurrent.futures

from numba import jit
import time


# 一种计算圆周率算法
@jit  # 通过JIT加速，更高效地执行CPU密集型运算
def compute_pi():
    # 因为Python程序执行速度是比较慢的（相对于所有编译型编程语言和大多数解
    # 释型编程语言），在做CPU密集型运算时显得更加吃力，所以我们在这里进行了
    # JIT加速，其原理就是在执行这段代码时先编译成机器码再执行，可以大大提高
    # 程序的运行速度如果该程序在您电脑上运行所需时间仍然较长，可适当调低
    # count的数值
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
    # 将计算圆周率（CPU密集型）的代码交给进程池执行器执行
    pi = await asyncio.get_running_loop().run_in_executor(
        pool,
        compute_pi
    )
    print(f"[{time.strftime('%X')}] {pi}")


async def task():
    for i in range(5):
        print(f"[{time.strftime('%X')}] Step {i}")
        await asyncio.sleep(1)


async def main():
    # 声明一个进程池执行器对象，与线程池执行器一样只需要声明一次，可以在多处使用
    pool = concurrent.futures.ProcessPoolExecutor()

    await asyncio.gather(
        # 将线程池对象pool传入给print_pi函数，由print_pi函数执行CPU密集
        # 型代码逻辑，并且我们将CPU密集型代码与异步代码并行执行
        print_pi(pool),
        task()
    )


if __name__ == '__main__':
    """
    这里需要判断只有在文件名为 __main__ 时才会执行主程序，为了避免在创建子
    进程时重复运行主程序而产生错误
    """
    asyncio.run(main())
