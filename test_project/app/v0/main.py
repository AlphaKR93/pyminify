from fastapi import FastAPI

from .router import router


app = FastAPI(version="0")
app.include_router(router)

@app.get("")
async def root():
    return {"version": "0"}
