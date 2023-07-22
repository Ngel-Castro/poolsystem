from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional, List

import datetime

router = APIRouter()


class PoolReadings(BaseModel):
    id: int
    pool_id: int
    operator_id: int
    ph: float
    chlorine: float
    salt: float
    date: datetime.datetime
    alkalinity: Optional[float] = None
    temperature: Optional[float] = None
    comments: Optional[str] = None
