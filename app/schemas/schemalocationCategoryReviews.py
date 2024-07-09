from pydantic import BaseModel
from datetime import datetime 
from typing import Optional


"""
    Esquema Pydantic base para la creación de una revisión de combinación de ubicación y categoría.

    Atributos:
        location_id (int): ID de la ubicación.
        category_id (int): ID de la categoría.
        reviewed_at (datetime, opcional): Fecha y hora de la revisión. Por defecto, la fecha y hora actual.
"""
class LocationCategoryReviewedBase(BaseModel):
    location_id: int
    category_id: int
    reviewed_at: Optional[datetime]= datetime

    class Config:
        orm_mode = True
"""
    Esquema Pydantic para actualizar la fecha de revisión de una combinación de ubicación y categoría.

    Atributos opcionales:
        location_id (int, opcional): Nuevo ID de ubicación, si se desea actualizar.
        category_id (int, opcional): Nuevo ID de categoría, si se desea actualizar.
        reviewed_at (datetime, opcional): Nueva fecha y hora de revisión, si se desea actualizar.
"""
class LocationCategoryReviewedBaseDate(BaseModel):
    location_id: Optional[int]  = None
    category_id: Optional[int] = None
    reviewed_at: Optional[datetime]= datetime

    class Config:
        orm_mode = True
"""
    Esquema Pydantic para la salida de una revisión de combinación de ubicación y categoría, incluyendo el ID.

    Hereda de LocationCategoryReviewedBase para reutilizar la validación de atributos.

    Atributos:
        id (int): Identificador único de la revisión.

    Config:
        orm_mode (bool): Habilita el modo ORM para permitir la serialización/deserialización
                         automática de objetos SQLAlchemy.
"""
class LocationCategoryReviewedOut(LocationCategoryReviewedBase):
    id: int

    class Config:
        orm_mode = True