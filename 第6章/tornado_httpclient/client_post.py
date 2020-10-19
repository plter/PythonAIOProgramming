"""
第6章/tornado_httpclient/client_post.py
"""
import tornado.httpclient
import asyncio

# 创建一个基于异步IO的HTTP客户端
client = tornado.httpclient.AsyncHTTPClient()


async def main():
    # 向服务器发送请求
    resp = await client.fetch(
        # 创建一个 POST 方式的请求，并将参数传给服务器
        tornado.httpclient.HTTPRequest(
            "http://127.0.0.1:8888",
            "POST",
            # POST 方式的请求可以附加较大的数据（一般不超过100M）
            # 将参数写在 body 中发送给服务器
            body="name=Xiaoming"
        )
    )
    print(resp.body.decode("utf-8"))


asyncio.run(main())
