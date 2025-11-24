from fastapi import APIRouter

from lib import hello_world


router = APIRouter(prefix="/router")

@router.get("/")
async def root():
    return {"message": await hello_world()}
