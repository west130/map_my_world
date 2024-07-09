from fastapi import FastAPI
from .db.dbConfiguration import engine, Base
from .routers import routerCategories, routerCombinations, routerLocations, routerRecommendations

# Este fragmento de código configura una aplicación FastAPI y define rutas para diferentes
# funcionalidades. Esto es lo que hace cada línea:
app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(routerLocations.router)
app.include_router(routerRecommendations.router)
app.include_router(routerCategories.router)
app.include_router(routerCombinations.router)
""" app.include_router(categories.router)
app.include_router(recommendations.router) """