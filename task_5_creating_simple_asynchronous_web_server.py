from aiohttp import web
import asyncio


async def handle_root(request):
    """Handles requests to the root route and returns a simple text."""
    return web.Response(text="Hello, World!")


async def handle_slow(request):
    """Handles requests to /slow, simulating a long operation with a 5 second delay."""
    await asyncio.sleep(5)
    return web.Response(text="Operation completed")

app = web.Application()
app.router.add_get('/', handle_root)
app.router.add_get('/slow', handle_slow)

if __name__ == "__main__":
    web.run_app(app, host="127.0.0.1", port=8080)
