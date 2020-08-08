async def app(scope, receive, send):
    request_type = scope['type']
    if request_type == 'http':
        await send({
            'type': 'http.response.start',
            'status': 200,
            'headers': [
                [b'content-type', b'text/html'],
            ]
        })
        await send({
            'type': 'http.response.body',
            'body': b"Hello World",
            'more_body': False
        })
    elif request_type == 'lifespan':
        while True:
            message = await receive()
            if message['type'] == 'lifespan.startup':
                await send({'type': 'lifespan.startup.complete'})
            elif message['type'] == 'lifespan.shutdown':
                await send({'type': 'lifespan.shutdown.complete'})
                break
    else:
        raise NotImplementedError()
