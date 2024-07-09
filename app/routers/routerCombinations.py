
from fastapi import APIRouter, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from fastapi import Depends
from ..db.dbConfiguration import getDB
from ..models.modelLocationCategoryReviewed import LocationCategoryReviewed
from ..schemas.schemalocationCategoryReviews import LocationCategoryReviewedBase, LocationCategoryReviewedOut, LocationCategoryReviewedBaseDate
router = APIRouter()
"""
    Crea una nueva combinación de ubicación-categoría revisada en la base de datos.

    Args:
        combination (LocationCategoryReviewedBase): Datos de la combinación a crear.
        db (Session, optional): Sesión de base de datos SQLAlchemy. Defaults to Depends(getDB).

    Returns:
        LocationCategoryReviewedOut: La combinación creada.
    
    Raises:
        HTTPException: Si ocurre un error en la base de datos.
"""
@router.post("/combinations", response_model=LocationCategoryReviewedOut)
def create_combinations(combination: LocationCategoryReviewedBase, db: Session = Depends(getDB)):
    try:
        db_combination = LocationCategoryReviewed(location_id=combination.location_id, category_id=combination.category_id)
        db.add(db_combination)
        db.commit()
        db.refresh(db_combination)
        return db_combination
    except SQLAlchemyError as e:
        error_message = str(e)
        raise HTTPException(
            status_code=500, detail="Error en la base de datos: " + error_message)
"""
    Actualiza una combinación de ubicación-categoría revisada existente en la base de datos.

    Args:
        combinations_id (int): ID de la combinación a actualizar.
        combination (LocationCategoryReviewedBaseDate): Datos actualizados de la combinación.
        db (Session, optional): Sesión de base de datos SQLAlchemy. Defaults to Depends(getDB).

    Returns:
        LocationCategoryReviewedOut: La combinación actualizada.
    
    Raises:
        HTTPException: Si la combinación no existe o si ocurre un error en la base de datos.
"""
@router.put("/combinations/{combinations_id}", response_model=LocationCategoryReviewedOut)
def update_combinations(combinations_id: int, combination: LocationCategoryReviewedBaseDate, db: Session = Depends(getDB)):
    try:
        db_location = db.query(LocationCategoryReviewed).filter(
            LocationCategoryReviewed.id == combinations_id).first()
        if not db_location:
            raise HTTPException(status_code=404)
        for field, value in vars(combination).items():
            if value is not None:
                setattr(db_location, field, value)
        db.commit()
        return db_location
    except SQLAlchemyError as e:
        error_message = str(e)
        raise HTTPException(
            status_code=500, detail="Error en la base de datos: " + error_message)

"""
    Elimina una combinación de ubicación-categoría revisada por su ID en la base de datos.

    Args:
        combinations_id (int): ID de la combinación a eliminar.
        db (Session, optional): Sesión de base de datos SQLAlchemy. Defaults to Depends(getDB).

    Returns:
        LocationCategoryReviewedOut: La combinación eliminada.
    
    Raises:
        HTTPException: Si la combinación no existe o si ocurre un error en la base de datos.
"""
@router.delete("/combinations/{combinations_id}", response_model=LocationCategoryReviewedOut)
def delete_combinations(combinations_id: int, db: Session = Depends(getDB)):
    try:
        db_location = db.query(LocationCategoryReviewed).filter(
            LocationCategoryReviewed.id == combinations_id).first()
        if db_location is None:
            raise HTTPException(status_code=404)
        db.delete(db_location)
        db.commit()
        return db_location
    except SQLAlchemyError as e:
        error_message = str(e)
        raise HTTPException(
            status_code=500, detail="Error en la base de datos: " + error_message)