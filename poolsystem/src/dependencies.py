from typing import Annotated

from fastapi import Header, HTTPException


async def get_token_header(x_token: Annotated[str, Header()]):
    """Validate token"""
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def get_query_token(token: str = None):
    """Get token from query"""
    if token != "ngel":
        raise HTTPException(status_code=400, detail="No token provided")
