# README

## API - Apiscope

Api formulada para la realización de cálculos de indicadores asociados a calidad de vida.

## Ejecución del proyecto

Para la correcta ejecución del proyecto, es aconsejable usar un entorno virtual e instalar las diferentes bibliotecas que se encuentran en el archivo **requirements.txt**.

    pip install -r requirements.txt

    
Y para ejecutar el proyecto se debe correr el siguiente comando en consola:

     python src/app.py

Para su prueba en local se debe encontrar las bases de datos, postgresql y mongodb funcionando, con las tablas y colecciones creadas y con los registros correspondientes de los indicadores, sus variables y los bloques asociados a ellas.
Junto a lo anterior, se debe de modificar las rutas de conexión de las bases de datos, con los valores correspondientes para su correcta conexión.

En MongoDB: 
```
connection='mongodb://username:password@localhost:27017/database_name?authSource=identification'
```
Y en PostgreSQL:
```
return psycopg2.connect(host=config('PGSQL_HOST'),user=config('PGSQL_USER'),password=config('PGSQL_PASSWORD'),database=config('PGSQL_DATABASE'))
```