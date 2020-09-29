"""
第1章/write_file.py
"""
import asyncio  # 引入 asyncio 模块


async def main():
    # 获取事件循环
    loop = asyncio.get_running_loop()
    # 将阻塞型 IO 的 open 函数运行在线程池执行器（ThreadPoolExecutor）中，
    # 以写入字符串的方式打开文件 data.txt
    f = await loop.run_in_executor(None, open, "data.txt", 'w')
    # 将数据写入到文件中
    await loop.run_in_executor(None, f.write, "aio file")
    # 关闭文件
    await loop.run_in_executor(None, f.close)


if __name__ == '__main__':
    asyncio.run(main())
