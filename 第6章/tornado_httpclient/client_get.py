"""
第6章/tornado_httpclient/client_get.py
"""

import tornado.httpclient
import asyncio

# 创建一个基于异步IO的HTTP客户端
client = tornado.httpclient.AsyncHTTPClient()


async def main():
    # 向服务器发送一个GET方式的请求
    resp = await client.fetch("http://127.0.0.1:8888?name=Xiaoming")
    # 将服务器返回的结果以 utf-8 的编码方式进行解码
    print(resp.body.decode("utf-8"))


asyncio.run(main())
