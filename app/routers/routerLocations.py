from fastapi import APIRouter, HTTPException
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from fastapi import Depends
from ..db.dbConfiguration import getDB
from ..models.modelLocations import Locations
from ..schemas.schemaLocations import LocationCreate, LocationOut, LocationUpdate

router = APIRouter()


@router.post("/locations", response_model=LocationOut)
def create_location(location: LocationCreate, db: Session = Depends(getDB)):
    try:
        db_location = Locations(
            latitude=location.latitude, longitude=location.longitude, name=location.name)
        db.add(db_location)
        db.commit()
        db.refresh(db_location)
        return db_location
    except SQLAlchemyError as e:
        error_message = str(e)
        raise HTTPException(
            status_code=500, detail="Error en la base de datos: " + error_message)


@router.get("/locations/all", response_model=list[LocationOut])
def get_all_location(db: Session = Depends(getDB)):
    try:
        db_location = db.query(Locations).all()
        if db_location is None:
            raise HTTPException(status_code=404)
        return db_location
    except SQLAlchemyError as e:
        error_message = str(e)
        raise HTTPException(
            status_code=500, detail="Error en la base de datos: " + error_message)


@router.get("/locations/{location_id}", response_model=list[LocationOut])
def get_location(location_id: int, db: Session = Depends(getDB)):
    try:
        db_location = db.query(Locations).filter_by(id=location_id).first()
        if db_location is None:
            raise HTTPException(status_code=404)
        return db_location
    except SQLAlchemyError as e:
        error_message = str(e)
        raise HTTPException(
            status_code=500, detail="Error en la base de datos: " + error_message)


# Consulta la ubicación existente por su ID
# Elimina la ubicacion
# Si la ubicación no existe, retornar el error
@router.delete("/locations/{location_id}")
def delete_location(location_id: int, db: Session = Depends(getDB)):
    try:
        db_location = db.query(Locations).filter(
            Locations.id == location_id).first()
        
        if db_location is None:
            raise HTTPException(status_code=404)
        db.delete(db_location)
        db.commit()
        return db_location
    except SQLAlchemyError as e:
        error_message = str(e)
        raise HTTPException(
            status_code=500, detail="Error en la base de datos: " + error_message)


# Consulta la ubicación existente por su ID
# Si la ubicación no existe, retornar el error
# Actualiza los campos de la ubicación con los valores proporcionados en location_update
# Confirma los cambios en la base de datos
# Retorna la ubicación actualizada
@router.put("/locations/{location_id}", response_model=LocationOut)
def update_location(location_id: int, location_update: LocationUpdate, db: Session = Depends(getDB)):
    try:
        db_location = db.query(Locations).filter(
            Locations.id == location_id).first()
        if not db_location:
            raise HTTPException(status_code=404)
        for field, value in vars(location_update).items():
            if value is not None:
                setattr(db_location, field, value)
        db.commit()
        return db_location
    except SQLAlchemyError as e:
        error_message = str(e)
        raise HTTPException(
            status_code=500, detail="Error en la base de datos: " + error_message)
