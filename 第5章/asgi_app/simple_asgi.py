"""
第5章/asgi_app/simple_asgi.py
"""


async def app(scope, receive, send):
    # 向前端发送HTTP协议头，包括了HTTP状态与协议头
    await send({
        'type': 'http.response.start',
        'status': 200,
        'headers': [
            [b'content-type', b'text/html'],
        ]
    })
    # 向前端发送数据，如果数据庞大，还可以分段发送
    await send({
        'type': 'http.response.body',
        'body': b"Hello World",
        'more_body': False
    })
