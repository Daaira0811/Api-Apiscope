from IndicatorsData.models.VariableModel import Variable
from IndicatorsData.db.postgresConfig import get_connection


class VariableController():

    def __init__(self):
        self.connection=get_connection()
    
    #Este método busca los bloques que tengan valores asociados de cierta variable, 
    #que se requiera para realizar el cálculo de cualquier indicador.
    def get_variable_from_Db(self,variable_number):
        try:
            variables=[]
            query="Select V.id_bloque, valor FROM variable_bloque V INNER JOIN bloque_mesa B ON V.id_bloque=B.id_bloque AND estado=true AND id_variable={}".format(variable_number)
            #Esta consulta valida que el id_bloque se encuentre dentro de la mesa y tenga el valor de la variable que se quiera buscar
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                resultset = cursor.fetchall()
                if (any(resultset)):   
                    for row in resultset:
                       
                # Se obtiene el radio de inlcuencia de cada variable
                        radio = VariableController.get_radio_influence(self,variable_number)
                        if (not any(row)):
                            ('any row')
                        else:
                            variable = Variable(row[0], row[1], radio)
                            variables.append(variable.to_JSON())
                    return variables
        except Exception as ex:
            raise Exception(ex) 
        
    #Función que obtiene el rango de incluencia de cierta variable
    def get_radio_influence(self,id_variable):
        try:
            query="SELECT radio_influencia FROM variable WHERE id_variable={}".format(id_variable)
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                resultset = cursor.fetchall()
            return resultset[0][0]
        except Exception as ex:
            raise Exception(ex)

#De acuerdo a los indicadores, asociados a la tabla, se buscan las variables a calcular de cada indicador
    def get_variables_from_indicators(self,id_indicator):
        try:
            variables=[]
            query="SELECT id_variable, nombre FROM formula WHERE id_indicador={}".format(id_indicator)
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                resultset = cursor.fetchall()
                for row in resultset:
                    variable = row[0], row[1]
                    variables.append(variable)
            return variables
        except Exception as ex:
            raise Exception(ex)