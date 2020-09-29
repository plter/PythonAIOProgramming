"""
第1章/aio_socket_client.py
"""

import asyncio
import time


async def main():
    # 通过 asyncio.open_connection 函数创建一个到
    # 本机8888端口的连接，可用于连接第1章/aio_socket_server.py
    # 所启动的服务器
    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 8888
    )

    # 通过循环不断地一行一行读取数据，并将读到的数据输出到终端里，
    # 在读到数据结尾时跳出循环
    while not reader.at_eof():
        # 读取一行数据
        data = await reader.readline()
        print(f"[{time.strftime('%X')}] Received: {data}")


asyncio.run(main())
