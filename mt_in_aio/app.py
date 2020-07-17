import asyncio
import time
import concurrent.futures


# 声明一个阻塞型任务
def blocked_task():
    for i in range(10):
        # 使用阻塞型时钟休眠来模拟阻塞型IO运行效果
        time.sleep(1)
        print(f"[{time.strftime('%X')}] Blocked task {i}")


# 声明一个异步任务
async def async_task():
    for i in range(2):
        await asyncio.sleep(5)
        print(f"[{time.strftime('%X')}] Async task {i}")


async def main():
    # 创建一个线程池执行器，该执行器所允许的最大线程数是5
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=5)

    # 获取当前正在运行的事件循环对象
    current_running_loop = asyncio.get_running_loop()

    # 并发执行一个阻塞型任务和一个异步任务
    await asyncio.gather(
        # 通过事件循环将该任务运行在特定的执行器（Executor）中
        current_running_loop.run_in_executor(executor, blocked_task),
        async_task()
    )


asyncio.run(main())
