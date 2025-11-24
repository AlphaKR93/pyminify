from os import getenv

from fastapi import FastAPI
from vercel.cache import AsyncRuntimeCache

from .v0 import app as _v0


if __debug__ and getenv("PYCHARM_DEBUG", "0") == "1":
    import pydevd_pycharm

    pydevd_pycharm.settrace('localhost', port=8399, stdout_to_server=True, stderr_to_server=True)

cache = AsyncRuntimeCache()
app = FastAPI()
app.mount("/v0", _v0)

@app.get("/")
async def root():
    await cache.get("test")
    return {"success": "Hello, world!"}
