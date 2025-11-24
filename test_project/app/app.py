from fastapi import FastAPI

from .v0 import app as _v0


app = FastAPI()
app.mount("/v0", _v0)

@app.get("")
async def root():
    return {"success": "Hello, world!"}
