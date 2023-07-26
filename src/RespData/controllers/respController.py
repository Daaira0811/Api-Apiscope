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
        
    def updateRespData():
        try:
            data ='["Areas verdes",["Area verde por habitantes","Bloque con indicador",1,"Bloques dentro del rango de influencia",[0,3,9,19],"Valor actual de personas dentro del area",112,"Valor optimo de personas dentro del area",3732,"Bloques sin influencia",[5,6,10]],"Educacion",["Equipos educacionales basicos","Bloque con indicador",32,"Bloques dentro del rango de influencia",[0,3,5,6,9,10,19],"Valor actual de personas dentro del area",215,"Valor optimo de personas dentro del area",12,"Bloques sin influencia",[]],"Educacion",["Equipos educacionales medios","Bloque con indicador",30,"Bloques dentro del rango de influencia",[0,3,5,6,9,10,19],"Valor actual de personas dentro del area",215,"Valor optimo de personas dentro del area",12,"Bloques sin influencia",[]],"Deportivos",["Gimnasios","Bloque con indicador",31,"Bloques dentro del rango de influencia",[0,3,5,6,9,10,19],"Valor actual de personas dentro del area",215,"Valor optimo de personas dentro del area",12,"Bloques sin influencia",[]]]' 
            id=mongo.insert_one({'data':data})
            return str(id)
        except Exception as ex:
            return Response(
                response= json.dumps({"message": "No se pueden actualizar los datos"}),
                status=500,
                mimetype='aplication/json'
            )