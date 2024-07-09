from fastapi import APIRouter, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from fastapi import Depends
from ..db.dbConfiguration import getDB
from ..models.modelCategories import Categories
from ..schemas.schemaCategory import CategoryCreate, CategoryOut, CategoryUpdate
router = APIRouter()
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