# Se agregan las funciones de obtener y actualizar el archivo data
import json
from flask import Response
from RespData.db.mongoConfig import init_app

mongo=init_app()

class RespController:
    def getRespData():
        try:
            response=mongo.find().sort("_id",-1).limit(1)
            data_json_str = response[0]['data']
            data_json = json.loads(data_json_str)
            return data_json
        except Exception as ex:
            print(ex)
            return Response(
                response= json.dumps({"message": "No se puede leer los datos"}),
                status=500,
                mimetype='aplication/json'
            )
        
    def updateRespData(data):
        try:
            id=mongo.insert_one({'data':data})
            return str(id)
        except Exception as ex:
            return Response(
                response= json.dumps({"message": "No se pueden actualizar los datos"}),
                status=500,
                mimetype='aplication/json'
            )