"""
第1章/aio_http_client/aio_http_client.py
"""
import asyncio


async def main():
    # open_connection 函数有两个返回值，reader 和 writer ，其中 reader 用
    # 于读取服务器的数据，writer用于向服务器发送数据
    reader, writer = await asyncio.open_connection("yunp.top", "80")
    # HTTP协议的第一行，指定请求资源及HTTP版本
    writer.write(b'GET / HTTP/1.0\r\n')
    # 发送 HTTP 协议头结尾标识
    writer.write(b'\r\n')

    # write 函数会尝试立即向 socket 连接发送数据，但是也有可能失败，最常见的原因
    # 是当前 IO 资源被占用，失败时数据以队列形式暂存于缓冲区直到可以被再次发送，为
    # 确保数据已经完全发送成功之后再做后续操作，通常使用 drain 函数来等待数据发送
    # 完毕，如果在调用该函数前数据已经发送完毕，则该函数立即返回结果
    await writer.drain()
    result = await reader.read()
    print(result.decode("utf-8"))


if __name__ == '__main__':
    asyncio.run(main())
