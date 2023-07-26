# Se agregan las funciones de obtener y actualizar los datos de los indicadores
from IndicatorsData.models.BlockModel import Block
from IndicatorsData.db.postgresConfig import get_connection
from flask import json, jsonify

class BlockController():
    
    def __init__(self):
        self.connection=get_connection()

##Esta función me retorna una lista de las coordenadas de todos los bloques de la mesa
    def get_coordinates_from_db(self,block_id):
        try:
            block=None
            with self.connection.cursor() as cursor:
                query="select A.cod_colores, latitud,longitud from bloque_mesa B inner Join bloque A ON B.id_bloque=A.id_bloque AND A.id_bloque={}".format(block_id)
                cursor.execute(query)
                resultset = cursor.fetchall()
                for row in resultset:
                   block= Block(block_id,row[0],row[1], row[2])
            return block.to_JSON()
        except Exception as ex:
            print('Error al buscar las coordenadas del id: '+ str(block_id))
            return jsonify({'message':str(ex)}), 500
           
        
    def get_coordinates_from_db_list(self,blocks_ids):
            try:
                blocks=[]
                for block_id in blocks_ids:
                    block=None
                    with self.connection.cursor() as cursor:
                        query="select A.cod_colores, latitud,longitud from bloque_mesa B inner Join bloque A ON B.id_bloque=A.id_bloque AND A.id_bloque={}".format(block_id)
                        cursor.execute(query)
                        resultset = cursor.fetchall()
                        print(resultset)
                        for row in resultset:
                            block= Block(block_id,row[0],row[1], row[2])
                            blocks.append(block.to_JSON())
                self.connection.commit()
                return json.dumps(blocks)
            except Exception as ex:
                raise Exception(ex)
                
                
# Modidicar el nombre de la mesa para que lo obtenga como parámetro de la configuración del proyecto

    def get_block_table(self):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("SELECT V.id_bloque_mesa, V.id_bloque , cod_colores FROM bloque_mesa V INNER JOIN bloque B ON V.id_bloque=B.id_bloque INNER JOIN mesa N ON V.id_mesa=N.id_mesa AND N.nombre='epanueve'")
                resultset = cursor.fetchall()
            return resultset
        except Exception as ex:
            raise Exception(ex)

#Se modidica la tabla bloque_mesa y se cambia el bloque por el valor que se tenga en la lista de bloques
    def update_block(self,data):
         for bloque in data.items():
            try:
                id_block=bloque[0]
                pattern=bloque[1]
                with self.connection.cursor() as cursor:
                    #Se debe buscar el bloque que tenga el patrón, se obtiene el id
                    cursor.execute("SELECT id_bloque FROM bloque WHERE cod_colores='"+pattern+"'")
                    #Se modifica el id dentro del id del bloque dentro de la tabla bloque_mesa
                    resultset = cursor.fetchall()
                    if resultset:
                        id_block_db=str(resultset[0][0])
                        query="UPDATE bloque_mesa SET id_bloque='"+id_block_db+"' WHERE id_bloque_mesa='"+str(id_block)+"'"
                        cursor.execute(query)
                    
                self.connection.commit()
            except Exception as ex:
                raise Exception(ex)