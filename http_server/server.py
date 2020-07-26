import asyncio


async def handle_connection(reader, writer):
    content = b'<html>' \
              b'  <head>' \
              b'    <title>Title</title>' \
              b'  </head>' \
              b'  <body>' \
              b'    Hello World' \
              b'  </body>' \
              b'</html>'
    # 设置http响应的状态，200是成功
    writer.write(b"HTTP/1.0 200 OK\r\n")
    # 指定http响应内容的长度
    writer.write(f"Content-Length: {len(content)}\r\n".encode('utf-8'))
    # 指定http响应内容的格式
    writer.write(b"Content-Type: text/html\r\n")
    # 头部结尾
    writer.write(b"\r\n")
    # 发送响应内容
    writer.write(content)
    # 等待发送完成
    await writer.drain()
    # 关闭连接
    writer.close()


async def main():
    async with (
            await asyncio.start_server(handle_connection, port=8888)
    ) as server:
        await server.serve_forever()


asyncio.run(main())
