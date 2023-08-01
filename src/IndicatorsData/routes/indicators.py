from flask import Blueprint, jsonify, request
from IndicatorsData.controllers.BlockController import BlockController
from IndicatorsData.controllers.IndicatorController import IndicatorController


indicators=Blueprint('indicators',__name__,url_prefix='/indicators')

blockController=BlockController()
indicator=IndicatorController()

#Se obtiene las coordenadas de cierto bloque
@indicators.route('/getCoordinates/<int:id>', methods=['GET'])
def getCoordinates(id):
    try:
        return blockController.get_coordinates_from_db(id)
    except Exception as ex:
        return jsonify('aa')
# Se obtiene las coordenadas de una lista de bloques
@indicators.route('/getCoordinates', methods=['GET'])
def getCoordinatesList():
    try:
        data= request.get_json()
        return blockController.get_coordinates_from_db_list(data)
    except Exception as ex:
        return jsonify({'message':str(ex)}), 500
    
# Se obtinenen todos los bloques de una tabla
@indicators.route('/getBlocks', methods=['GET'])
def getBlocks():
    try:
        return blockController.get_block_table()
    except Exception as ex:
        return jsonify({'message':str(ex)}), 500
    
# Se actualiza la tabla bloque_mesa con el id del bloque correspondiente al geogriddata
@indicators.route('/updateBlock', methods=['POST'])
def updateBlocks():
    try:
        data= request.get_json()
        blockController.update_block(data)
        return data
    except Exception as ex:
        return jsonify({'message':str(ex)}), 500
    
# Se obtiene la lista de indicadores
@indicators.route('/getIndicators', methods=['GET'])
def getIndicators():
    try:
        return indicator.get_indicators()
    except Exception as ex:
        return jsonify({'message':str(ex)}), 500