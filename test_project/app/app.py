from fastapi import FastAPI as B
from .A import D

A = B()
A.mount("/v0", D)


@A.get("/")
async def C():
    return {"success": "Hello, world!"}


app = A
