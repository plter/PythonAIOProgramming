"""
第2章/aio_http_server/aio_http_server.py
"""

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
    # 指定头部信息结束，后面的信息就是内容HTTP协议标准规定，当读到\r\n\r\n时，便认定是头部结束
    writer.write(b"\r\n")
    # 发送响应内容
    writer.write(content)
    # 等待发送完成
    await writer.drain()
    # 关闭连接
    writer.close()


async def main():
    async with (
            # 配置服务器端口
            await asyncio.start_server(handle_connection, port=8888)
    ) as server:
        # 启动服务器
        await server.serve_forever()


asyncio.run(main())
