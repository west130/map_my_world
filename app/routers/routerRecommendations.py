from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func, and_, exists
from datetime import datetime, timedelta
from ..db.dbConfiguration import getDB
from ..models.modelLocationCategoryReviewed import LocationCategoryReviewed
from ..models.modelCategories import Categories
from ..models.modelLocations import Locations
from ..schemas.schemalocationCategoryReviews import LocationCategoryReviewedOut
router = APIRouter()

"""
    Obtiene recomendaciones de combinaciones de ubicación-categoría que no han sido revisadas en los últimos 30 días.

    Args:
        db (Session, optional): Sesión de base de datos SQLAlchemy. Defaults to Depends(getDB).

    Returns:
        list[LocationCategoryReviewedOut]: Lista de recomendaciones de combinaciones de ubicación-categoría.
    
    Raises:
        HTTPException: Si ocurre un error en la base de datos.
"""
@router.get("/recommendations", response_model=list[LocationCategoryReviewedOut])
def get_recommendations(db: Session = Depends(getDB)):
    thirty_days_ago = datetime.now() - timedelta(days=30)

    # Subquery para obtener las combinaciones de ubicación-categoría revisadas en los últimos 30 días
    subquery = db.query(LocationCategoryReviewed.location_id, LocationCategoryReviewed.category_id) \
                .filter(LocationCategoryReviewed.reviewed_at >= thirty_days_ago) \
                .subquery()

    # Consulta para obtener las combinaciones no revisadas en los últimos 30 días, priorizando las que nunca se han revisado
    recommendations = db.query(LocationCategoryReviewed)\
                        .join(Locations, Locations.id == LocationCategoryReviewed.location_id) \
                        .join(Categories, Categories.id == LocationCategoryReviewed.category_id) \
                        .filter(and_(
                            LocationCategoryReviewed.reviewed_at < thirty_days_ago,
                            ~exists().where(and_(
                                subquery.c.location_id == LocationCategoryReviewed.location_id,
                                subquery.c.category_id == LocationCategoryReviewed.category_id
                            ))
                        )) \
                        .limit(10) \
                        .all()

    return recommendations