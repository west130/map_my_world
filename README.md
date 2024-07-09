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
