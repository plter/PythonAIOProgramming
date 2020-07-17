import asyncio


async def main():
    reader, writer = await asyncio.open_connection("yunp.top", "80")
    writer.write(b'GET / HTTP/1.0\r\n')  # HTTP协议的第一行，指定请求资源及HTTP版本
    writer.write(b'\r\n')  # HTTP协议头部结尾标识
    await writer.drain()
    result = await reader.read()
    print(result.decode("utf-8"))


if __name__ == '__main__':
    asyncio.run(main())
