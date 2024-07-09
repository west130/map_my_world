from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from ..db.dbConfiguration import Base
"""
    Modelo de SQLAlchemy para la tabla 'locations'.

    Attributes:
        id (int): Identificador único de la ubicación (clave primaria).
        name (str): Nombre único de la ubicación.
        latitude (float): Coordenada de latitud de la ubicación.
        longitude (float): Coordenada de longitud de la ubicación.
        reviews (RelationshipProperty): Relación con las revisiones de ubicaciones.
"""
class Locations(Base):
    __tablename__ = 'locations'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=True)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    reviews = relationship("LocationCategoryReviewed", back_populates="location")