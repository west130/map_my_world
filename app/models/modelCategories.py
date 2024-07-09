
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from ..db.dbConfiguration import Base
"""
    Modelo de SQLAlchemy para la tabla 'categories'.

    Attributes:
        id (int): Identificador único de la categoría (clave primaria).
        name (str): Nombre único de la categoría.
        reviews (RelationshipProperty): Relación con las revisiones de ubicación-categoría asociadas.
"""
class Categories(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    reviews = relationship("LocationCategoryReviewed", back_populates="category")