import psycopg2
from psycopg2 import DatabaseError
from decouple import config

# Conexión a postgresql

def get_connection():
    try:
        print("Conectando a BD postgresql")
        return psycopg2.connect(
            host=config('PGSQL_HOST'),
            user=config('PGSQL_USER'),
            password=config('PGSQL_PASSWORD'),
            database=config('PGSQL_DATABASE')
        )
    except DatabaseError as ex:
        print("Conexión no lograda")
        raise Exception(ex)