from fastapi import APIRouter, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from fastapi import Depends
from ..db.dbConfiguration import getDB
from ..models.modelCategories import Categories
from ..schemas.schemaCategory import CategoryCreate, CategoryOut, CategoryUpdate
router = APIRouter()

"""
    Crea una nueva categoría en la base de datos.

    Args:
        category (CategoryCreate): Datos de la categoría a crear.
        db (Session, optional): Sesión de base de datos SQLAlchemy. Defaults to Depends(getDB).

    Returns:
        CategoryCreate: La categoría creada.
    
    Raises:
        HTTPException: Si ocurre un error en la base de datos.
"""
@router.post("/categories", response_model=CategoryCreate)
def create_category(categorie: CategoryCreate, db: Session = Depends(getDB)):
    try:
        db_category = Categories(name=categorie.name)
        db.add(db_category)
        db.commit()
        db.refresh(db_category)
        return db_category
    except SQLAlchemyError as e:
        error_message = str(e)
       
        raise HTTPException(
            status_code=500, detail="Error en la base de datos: " + error_message)
"""
    Obtiene todas las categorías almacenadas en la base de datos.

    Args:
        db (Session, optional): Sesión de base de datos SQLAlchemy. Defaults to Depends(getDB).

    Returns:
        list[CategoryOut]: Lista de todas las categorías.
    
    Raises:
        HTTPException: Si ocurre un error en la base de datos.
"""
@router.get("/categories/all", response_model=list[CategoryOut])
def get_all_categories(db: Session = Depends(getDB)):
    try:
        db_category = db.query(Categories).all()
        if db_category is None:
            raise HTTPException(status_code=404)
        return db_category
    except SQLAlchemyError as e:
        error_message = str(e)
        raise HTTPException(
            status_code=500, detail="Error en la base de datos: " + error_message)
"""
    Obtiene una categoría específica por su ID desde la base de datos.

    Args:
        category_id (int): ID de la categoría a obtener.
        db (Session, optional): Sesión de base de datos SQLAlchemy. Defaults to Depends(getDB).

    Returns:
        CategoryOut: La categoría encontrada.
    
    Raises:
        HTTPException: Si la categoría no existe o si ocurre un error en la base de datos.
"""
@router.get("/categories/{category_id}", response_model=list[CategoryOut])
def get_category(category_id: int, db: Session = Depends(getDB)):
    try:
        db_category = db.query(Categories).filter_by(id=category_id).first()
        if db_category is None:
            raise HTTPException(status_code=404)
        return db_category
    except SQLAlchemyError as e:
        error_message = str(e)
        raise HTTPException(
            status_code=500, detail="Error en la base de datos: " + error_message)  

"""
    Elimina una categoría específica por su ID desde la base de datos.

    Args:
        category_id (int): ID de la categoría a eliminar.
        db (Session, optional): Sesión de base de datos SQLAlchemy. Defaults to Depends(getDB).

    Returns:
        CategoryOut: La categoría eliminada.
    
    Raises:
        HTTPException: Si la categoría no existe o si ocurre un error en la base de datos.
"""
@router.delete("/categories/{category_id}", response_model=CategoryOut)
def delete_category(category_id: int, db: Session = Depends(getDB)):
    try:
        db_category = db.query(Categories).filter(Categories.id == category_id).first()
        if db_category is None:
            raise HTTPException(status_code=404)
        db.delete(db_category)
        db.commit()
        return db_category
    except SQLAlchemyError as e:
        error_message = str(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error en la base de datos: " + error_message)  

"""
    Actualiza una categoría específica por su ID en la base de datos.

    Args:
        category_id (int): ID de la categoría a actualizar.
        category_update (CategoryUpdate): Datos actualizados de la categoría.
        db (Session, optional): Sesión de base de datos SQLAlchemy. Defaults to Depends(getDB).

    Returns:
        CategoryOut: La categoría actualizada.
    
    Raises:
        HTTPException: Si la categoría no existe o si ocurre un error en la base de datos.
"""
@router.put("/categories/{category_id}", response_model=CategoryOut)
def update_category(category_id: int, category_update: CategoryUpdate, db: Session = Depends(getDB)):
    try:
        db_category = db.query(Categories).filter(
            Categories.id == category_id).first()
        if not db_category:
            raise HTTPException(status_code=404)
        for field, value in vars(category_update).items():
            if value is not None:
                setattr(db_category, field, value)
        db.commit()
        return db_category
    except SQLAlchemyError as e:
        error_message = str(e)
        raise HTTPException(
            status_code=500, detail="Error en la base de datos: " + error_message)