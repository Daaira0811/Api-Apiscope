from flask_pymongo import PyMongo
from pymongo import MongoClient

# Conexión a mongodb
def init_app():
    try:
        connection= 'mongodb://root:ap1scop3@apiscope_data:27017/apiscope_data?authSource=admin'
        client= MongoClient(connection)
        db=client.apiscope_data.data
        return db
    except Exception as ex:
        print(ex)
        print("Error - No se pudo conectar a la base de datos ")
