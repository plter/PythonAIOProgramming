"""
第1章/aio_socket_server.py
"""

import asyncio


async def handle_echo(reader, writer):
    """
    handle_echo 向客户端发送5段数据，时间间隔为1s，之后关闭客户端连接。
    :param reader: reader是一个StreamReader对象，用于读取客户端传来的数据。
    :param writer: writer是一个StreamWriter对象，用于向客户端发送数据。
    """

    # 向客户端输出5次数据
    for i in range(1, 6):
        writer.write(f'Count {i}\n'.encode('utf-8'))
        # 发送并等待数据发送成功
        await writer.drain()
        # 休眠1s
        await asyncio.sleep(1)

    writer.close()  # 关闭客户端连接


async def main():
    # 声明端口
    port = 8888
    # 启动服务器并注册一个回调函数用于侦听客户端连接，当有一个新的
    # 客户端建立连接时，将触发handle_echo函数。
    server = await asyncio.start_server(
        # 客户端连接的回调函数
        handle_echo,
        # 指定端口
        port=port
    )
    print(f'Serving on port {port}')
    async with server:
        # 开始接受连接
        await server.serve_forever()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:  # 用户强制退出时捕获该异常
        print("User stopped server")
