
from pydantic import BaseModel
from datetime import datetime 
from typing import Optional

class LocationCreate(BaseModel):
    latitude: float
    longitude: float
    name: str

class LocationUpdate(BaseModel):
    name: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    category_id: Optional[int] = None

class LocationOut(LocationCreate):
    id: int
    latitude: float
    longitude: float
    class Config:
        orm_mode = True