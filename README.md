# Map My World






### Prerequisitos 
###### Version de python: python3.10
##### Configura tu ambiente venv:
python3 -m venv venv
##### Clona el repositorio desde GitHub:

```
git clone https://github.com/west130/map_my_world
cd map-my-world
```

### Instalacion

##### Instala las dependencias:

```
pip install -r requirements.txt
```

##### Configura la base de datos:

Asegúrate de configurar adecuadamente tu base de datos según las instrucciones proporcionadas en db/dbConfiguration.py.
##### Ejecuta la aplicación:
```
uvicorn app.main:app --reload
```
### Endpoints Disponibles
##### Ubicaciones
```
GET /locations/all: Obtiene todas las ubicaciones.
GET /locations/{location_id}: Obtiene una ubicación por su ID.
POST /locations: Crea una nueva ubicación.
PUT /locations/{location_id}: Actualiza una ubicación existente.
DELETE /locations/{location_id}: Elimina una ubicación por su ID.
```
##### Recomendaciones
```
GET /recommendations: Obtiene recomendaciones de ubicaciones no revisadas en los últimos 30 días.
```
##### Categorías
```
GET /categories/all: Obtiene todas las categorías.
GET /categories/{category_id}: Obtiene una categoría por su ID.
POST /categories: Crea una nueva categoría.
PUT /categories/{category_id}: Actualiza una categoría existente.
DELETE /categories/{category_id}: Elimina una categoría por su ID.
```
##### Combinaciones
```
POST /combinations: Crea una nueva combinación de ubicación y categoría.
PUT /combinations/{combination_id}: Actualiza una combinación de ubicación y categoría por su ID.
DELETE /combinations/{combination_id}: Elimina una combinación de ubicación y categoría por su ID.
```
### Tecnologías Utilizadas
```
FastAPI: Framework web para construir APIs rápidas con Python 3.7+.
SQLAlchemy: ORM para interactuar con la base de datos SQL.
SQLite: Motor de base de datos ligero utilizado en desarrollo.
Pydantic: Para la validación de esquemas (schemas) y serialización de datos.
```