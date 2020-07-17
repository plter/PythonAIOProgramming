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
    # 创建第一个任务，不等待执行结束
    asyncio.create_task(task("task1", 1))
    # 创建第二个任务，并等待该任务执行结束
    await asyncio.create_task(task("task2", 2))


asyncio.run(main())
