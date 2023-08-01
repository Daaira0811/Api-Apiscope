from flask import Blueprint, jsonify, request
from RespData.controllers.respController import RespController

respData=Blueprint('respData',__name__,url_prefix='/respData')

@respData.route('/getData', methods=['GET'])
def get_data():
    try:
        return RespController.getRespData()
    except Exception as ex:
        return jsonify({'message':str(ex)}), 500
    
@respData.route('/updateData', methods=['POST'])
def post_data():
    try:
        data= request.get_json()
        return RespController.updateRespData(data)
    except Exception as ex:
        return jsonify({'message':str(ex)}), 500