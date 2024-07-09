from pydantic import BaseModel
from typing import Optional
"""
    Esquema Pydantic para crear una nueva categoría.

    Atributos:
        name (str): Nombre de la categoría.
"""
class CategoryCreate(BaseModel):
    name: str

"""
    Esquema Pydantic para la salida de categoría, incluyendo el ID.

    Hereda de CategoryCreate para reutilizar la validación del atributo 'name'.

    Atributos:
        id (int): Identificador único de la categoría.

    Config:
        orm_mode (bool): Habilita el modo ORM para permitir la serialización/deserialización
                         automática de objetos SQLAlchemy.
"""
class CategoryOut(CategoryCreate):
    id: int

    class Config:
        orm_mode = True
"""
    Esquema Pydantic para actualizar una categoría existente.

    Atributos opcionales:
        name (str, opcional): Nuevo nombre de la categoría, si se desea actualizar.
"""
class CategoryUpdate(BaseModel):
    name: Optional[str] = None


