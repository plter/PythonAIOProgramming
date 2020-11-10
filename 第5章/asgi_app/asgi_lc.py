"""
第5章/asgi_app/asgi_lc.py
"""


async def app(scope, receive, send):
    request_type = scope['type']
    if request_type == 'lifespan':
        while True:
            message = await receive()
            if message['type'] == 'lifespan.startup':
                await send({'type': 'lifespan.startup.complete'})
            elif message['type'] == 'lifespan.shutdown':
                await send({'type': 'lifespan.shutdown.complete'})
                break
