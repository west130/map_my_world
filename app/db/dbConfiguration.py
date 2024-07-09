from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL de la base de datos SQLite
DATABASE_URL = "sqlite:///./test.db"

# Crear el motor de la base de datos
engine = create_engine(DATABASE_URL)

# Declarar una clase base para la definición de modelos
Base = declarative_base()

# Crear una clase SessionLocal para manejar sesiones de base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
"""
    Función para obtener una sesión de base de datos.

    Returns:
        session: Sesión de base de datos SQLAlchemy.
"""
def getDB():
    db = SessionLocal()
    return db
