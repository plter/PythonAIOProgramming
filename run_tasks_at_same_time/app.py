import asyncio
import time


# 声明一个异步函数用于运行一个独立的任务
async def task(tag, delay):
    # 循环6次执行输出语句
    for i in range(6):
        # 根据delay参数休眠，delay的值以秒为单位
        await asyncio.sleep(delay)
        print(f"[{time.strftime('%X')}]Task:{tag}, step {i}")


async def main():
    # 并发执行多个任务
    await asyncio.gather(
        task("task1", 1),
        task("task2", 2)
    )


asyncio.run(main())
