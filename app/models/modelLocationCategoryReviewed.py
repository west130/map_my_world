from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from ..db.dbConfiguration import Base
class LocationCategoryReviewed(Base):
    __tablename__ = 'location_category_reviewed'
    id = Column(Integer, primary_key=True, index=True)
    location_id = Column(Integer, ForeignKey('locations.id'), nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)
    reviewed_at = Column(DateTime, default=datetime.utcnow)
    location = relationship("Locations", back_populates="reviews")
    category = relationship("Categories", back_populates="reviews")