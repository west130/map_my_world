from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from ..db.dbConfiguration import Base
"""
    Modelo de SQLAlchemy para la tabla 'location_category_reviewed'.

    Attributes:
        id (int): Identificador único de la combinación ubicación-categoría (clave primaria).
        location_id (int): ID de la ubicación asociada (clave foránea).
        category_id (int): ID de la categoría asociada (clave foránea).
        reviewed_at (datetime): Fecha y hora en que se revisó la combinación (por defecto, actual en UTC).
        location (RelationshipProperty): Relación con la ubicación asociada.
        category (RelationshipProperty): Relación con la categoría asociada.
"""
class LocationCategoryReviewed(Base):
    __tablename__ = 'location_category_reviewed'
    id = Column(Integer, primary_key=True, index=True)
    location_id = Column(Integer, ForeignKey('locations.id'), nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)
    reviewed_at = Column(DateTime, default=datetime.utcnow)
    location = relationship("Locations", back_populates="reviews")
    category = relationship("Categories", back_populates="reviews")