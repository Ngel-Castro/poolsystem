from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from typing import Optional, List
from ..dependencies import get_token_header

import datetime

router = APIRouter(
    prefix="/pool",
    tags=["pool"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


class Pool(BaseModel):
    id: int
    name: str
    address: str
    city: str
    state: Optional[str] = None
    zipcode: Optional[str] = None
    phone: str
    owner: int
    created: datetime.datetime
    modified: datetime.datetime


@router.get("/")
async def read_pools():
    """Get a pools from database"""
    return {"message": "Get all pools"}
