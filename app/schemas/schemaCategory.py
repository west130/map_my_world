from pydantic import BaseModel
from typing import Optional
# La clase `LocationOut` extiende `LocationCreate` e incluye un campo `id` adicional con el modo ORM
# habilitado.





# Esquema para crear una categoría
class CategoryCreate(BaseModel):
    name: str

# Esquema para representar una categoría, incluye el ID
class CategoryOut(CategoryCreate):
    id: int

    class Config:
        orm_mode = True

class CategoryUpdate(BaseModel):
    name: Optional[str] = None


