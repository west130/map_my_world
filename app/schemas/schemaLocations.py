
from pydantic import BaseModel
from datetime import datetime 
from typing import Optional
"""
    Esquema Pydantic para la creación de ubicaciones.

    Atributos:
        latitude (float): Latitud de la ubicación.
        longitude (float): Longitud de la ubicación.
        name (str): Nombre de la ubicación.
"""
class LocationCreate(BaseModel):
    latitude: float
    longitude: float
    name: str
"""
    Esquema Pydantic para actualizar una ubicación.

    Atributos opcionales:
        name (str, opcional): Nuevo nombre de la ubicación.
        latitude (float, opcional): Nueva latitud de la ubicación.
        longitude (float, opcional): Nueva longitud de la ubicación.
        category_id (int, opcional): Nuevo ID de categoría, si se desea actualizar.
"""
class LocationUpdate(BaseModel):
    name: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    category_id: Optional[int] = None
"""
    Esquema Pydantic para la salida de una ubicación, incluyendo el ID.

    Hereda de LocationCreate para reutilizar la validación de atributos de creación de ubicación.

    Atributos:
        id (int): Identificador único de la ubicación.
"""
class LocationOut(LocationCreate):
    id: int
    latitude: float
    longitude: float
    class Config:
        orm_mode = True