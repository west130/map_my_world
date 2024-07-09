from fastapi import FastAPI
from .db.dbConfiguration import engine, Base
from .routers import routerCategories, routerCombinations, routerLocations, routerRecommendations


app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(routerLocations.router, tags=["Ubicaciones"])
app.include_router(routerRecommendations.router, tags=["Recomendaciones"])
app.include_router(routerCategories.router, tags=["Categorías"])
app.include_router(routerCombinations.router, tags=["Combinaciones"])
