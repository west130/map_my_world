from fastapi import APIRouter, HTTPException
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from fastapi import Depends
from ..db.dbConfiguration import getDB
from ..models.modelLocations import Locations
from ..schemas.schemaLocations import LocationCreate, LocationOut, LocationUpdate

router = APIRouter()
"""
    Crea una nueva ubicación en la base de datos.

    Args:
        location (LocationCreate): Datos de la ubicación a crear.
        db (Session, optional): Sesión de base de datos SQLAlchemy. Defaults to Depends(getDB).

    Returns:
        LocationOut: La ubicación creada.

    Raises:
        HTTPException: Si ocurre un error en la base de datos.
"""
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
"""
    Obtiene todas las ubicaciones almacenadas en la base de datos.

    Args:
        db (Session, optional): Sesión de base de datos SQLAlchemy. Defaults to Depends(getDB).

    Returns:
        list[LocationOut]: Lista de todas las ubicaciones.
    
    Raises:
        HTTPException: Si ocurre un error en la base de datos.
"""
@router.get("/locations/all", response_model=list[LocationOut])
def get_all_location(db: Session = Depends(getDB)):

    try:
        db_location = db.query(Locations).all()
        if not db_location:
            raise HTTPException(
                status_code=404, detail="No se encontraron ubicaciones.")
        return db_location
    except SQLAlchemyError as e:
        error_message = str(e)
        raise HTTPException(
            status_code=500, detail="Error en la base de datos: " + error_message)
"""
    Obtiene una ubicación específica por su ID.

    Args:
        location_id (int): ID de la ubicación a obtener.
        db (Session, optional): Sesión de base de datos SQLAlchemy. Defaults to Depends(getDB).

    Returns:
        LocationOut: La ubicación solicitada.
    
    Raises:
        HTTPException: Si la ubicación no existe en la base de datos.
"""
@router.get("/locations/{location_id}", response_model=LocationOut)
def get_location(location_id: int, db: Session = Depends(getDB)):

    try:
        db_location = db.query(Locations).filter_by(id=location_id).first()
        if not db_location:
            raise HTTPException(
                status_code=404, detail=f"No se encontró la ubicación con ID {location_id}.")
        return db_location
    except SQLAlchemyError as e:
        error_message = str(e)
        raise HTTPException(
            status_code=500, detail="Error en la base de datos: " + error_message)
"""
    Elimina una ubicación específica por su ID de la base de datos.

    Args:
        location_id (int): ID de la ubicación a eliminar.
        db (Session, optional): Sesión de base de datos SQLAlchemy. Defaults to Depends(getDB).

    Returns:
        LocationOut: La ubicación eliminada.
    
    Raises:
        HTTPException: Si la ubicación no existe en la base de datos o si ocurre un error en la base de datos.
"""
@router.delete("/locations/{location_id}")
def delete_location(location_id: int, db: Session = Depends(getDB)):

    try:
        db_location = db.query(Locations).filter(
            Locations.id == location_id).first()

        if not db_location:
            raise HTTPException(
                status_code=404, detail=f"No se encontró la ubicación con ID {location_id}.")

        db.delete(db_location)
        db.commit()
        return db_location
    except SQLAlchemyError as e:
        error_message = str(e)
        raise HTTPException(
            status_code=500, detail="Error en la base de datos: " + error_message)
"""
    Actualiza una ubicación específica por su ID en la base de datos.

    Args:
        location_id (int): ID de la ubicación a actualizar.
        location_update (LocationUpdate): Datos actualizados de la ubicación.
        db (Session, optional): Sesión de base de datos SQLAlchemy. Defaults to Depends(getDB).

    Returns:
        LocationOut: La ubicación actualizada.
    
    Raises:
        HTTPException: Si la ubicación no existe en la base de datos o si ocurre un error en la base de datos.
"""
@router.put("/locations/{location_id}", response_model=LocationOut)
def update_location(location_id: int, location_update: LocationUpdate, db: Session = Depends(getDB)):

    try:
        db_location = db.query(Locations).filter(
            Locations.id == location_id).first()

        if not db_location:
            raise HTTPException(
                status_code=404, detail=f"No se encontró la ubicación con ID {location_id}.")

        for field, value in vars(location_update).items():
            if value is not None:
                setattr(db_location, field, value)

        db.commit()
        return db_location
    except SQLAlchemyError as e:
        error_message = str(e)
        raise HTTPException(
            status_code=500, detail="Error en la base de datos: " + error_message)
