from fastapi import APIRouter

root_route = APIRouter()

@root_route.get("/", tags=["Root"])
async def read_root():
    return {"message": "Hello, this is Arkan"}