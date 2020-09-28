"""
第1章/support_blocked_io.py
"""
import asyncio
import time
import concurrent.futures


# 声明一个阻塞型任务
def blocked_task():
    for i in range(10):
        # 为了简化代码逻辑，便于我们更加清晰地认识混合执行阻塞与非阻塞（异步）代
        # 码，这里以time.sleep函数来模拟阻塞型IO逻辑的执行效果。
        time.sleep(1)
        print(f"[{time.strftime('%X')}] Blocked task {i}")


# 声明一个异步任务
async def async_task():
    for i in range(2):
        await asyncio.sleep(5)
        print(f"[{time.strftime('%X')}] Async task {i}")


async def main():
    # 获取当前正在运行的事件循环对象，那么什么是事件循环，在1.1节中讲过协程是由
    # 事件机制驱动的，而用于驱动协程的事件机制系统在Python中被称为
    # 事件循环（Running Loop），通过该事件循环对象可以与其它线程或进程能行沟通。
    current_running_loop = asyncio.get_running_loop()

    # 并发执行一个阻塞型任务和一个异步任务
    await asyncio.gather(
        # 通过函数run_in_executor可以让指定的函数运行在特定的执行器（Executor）
        # 中，例如线程池执行器（concurrent.futures.ThreadPoolExecutor）或者
        # 进程池执行器（concurrent.futures.ProcessPoolExecutor）。
        current_running_loop.run_in_executor(None, blocked_task),
        async_task()
    )


asyncio.run(main())
