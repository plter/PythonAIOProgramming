from starlette.applications import Starlette
from starlette.responses import HTMLResponse
from starlette.routing import Route


async def homepage(request):
    return HTMLResponse("Hello World")


app = Starlette(debug=True, routes=[
    Route('/', homepage),
])
