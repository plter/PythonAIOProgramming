import asyncio


async def handle_echo(reader, writer):
    for i in range(1, 6):  # 向客户端输出5次数据
        writer.write(f'Count {i}\n'.encode('utf-8'))
        await writer.drain()  # 发送并等待数据发送成功
        await asyncio.sleep(1)  # 休眠1秒

    writer.close()  # 关闭客户端连接


async def main():
    port = 8888  # 声明端口
    server = await asyncio.start_server(  # 启动服务器
        handle_echo,  # 客户端连接的回调函数
        port=port  # 指定端口
    )
    print(f'Serving on port {port}')
    async with server:
        await server.serve_forever()  # 开始接受连接


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:  # 用户强制退出时捕获该异常
        print("User stopped server")
