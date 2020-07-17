import asyncio
import time


async def main():
    # 与服务器建立异步连接
    reader, writer = await asyncio.open_connection('127.0.0.1', 8888)

    while not reader.at_eof():
        data = await reader.readline()  # 一行一行读取
        print(f"[{time.strftime('%X')}] Received: {data}")


asyncio.run(main())
