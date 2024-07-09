from pydantic import BaseModel
from datetime import datetime 
from typing import Optional

class LocationCategoryReviewedBase(BaseModel):
    location_id: int
    category_id: int
    reviewed_at: Optional[datetime]= datetime

    class Config:
        orm_mode = True
class LocationCategoryReviewedBaseDate(BaseModel):
    reviewed_at: Optional[datetime]= datetime

    class Config:
        orm_mode = True
class LocationCategoryReviewedOut(LocationCategoryReviewedBase):
    id: int

    class Config:
        orm_mode = True