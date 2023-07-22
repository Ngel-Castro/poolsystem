import uvicorn
from fastapi import Depends, FastAPI
from .dependencies import get_token_header, get_query_token
from .routers import pool, pool_readings

app = FastAPI(dependencies=[Depends(get_query_token)])

app.include_router(pool.router)
# app.include_router(items.router)


@app.get("/")
async def root():
    """Root endpoint"""
    return {"message": "Welcome to the Pool API!"}


def start():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("poolsystem.src.main:app", host="localhost", port=8000, reload=True)
