from IndicatorsData.db.postgresConfig import get_connection
from IndicatorsData.models.IndicatorModel import Indicator
from decouple import config
from IndicatorsData.controllers.VariableController import VariableController

class IndicatorController():
    def __init__(self):
        self.connection=get_connection()



    #Esta función busca los indicadores que se encuentren dentro de la tabla
    def get_Indicators_from_Db(self):
        try:
            indicators=[]
            query="SELECT V.id_indicador, B.nombre FROM indicador_mesa V  INNER JOIN indicador B ON V.id_indicador=B.id_indicador INNER JOIN mesa N ON V.id_mesa=N.id_mesa AND N.nombre={}".format(config('Tablename'))
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                resultset = cursor.fetchall()
                for row in resultset:
                    indicator = Indicator(row[0], row[1])
                    indicators.append(indicator.to_JSON())
            return indicators
        except Exception as ex:
            raise Exception(ex)
        
    #Función que de acuerdo a los indicadores asociados a la mesa , retorna los bloques que estén asociados a las variables de cada indicador
    def get_indicators(self):
        variableController=VariableController()
        listBlocks=[]
        #Se obtiene la lista de bloques con habitantes
        listBlocks.append(variableController.get_variable_from_Db(1))
        #Se obtinene los indicadores y los id de sus variables asociadas
        indicators=IndicatorController.get_Indicators_from_Db(self)
    
        for i in indicators:
            idIndicator= i['id']
            nameIndicator=i['nombre']
            # Se obtiene el id de cada variable asociada a cada indicador en concreto
            variables=(variableController.get_variables_from_indicators(idIndicator))
            for variable in variables:
                idVariable=variable[0]
                nameVariable=variable[1]
                listaBloquesConUnaVariable=[]
                # Se obtienen los bloques aociados al id de cada variable
                if(idVariable!=1):
                    listaBloquesConUnaVariable.append(nameVariable)
                    listaBloquesConUnaVariable.append(variableController.get_variable_from_Db(idVariable)) # Se hace la consulta por las variables que tengan bloques activos asociddos en la base de datos
                    if(listaBloquesConUnaVariable[1] is not None): #Si los bloques asociados a la variable no son nulos, se agregan a la listaBloques
                        listBlocks.append(nameIndicator)
                        listBlocks.append(listaBloquesConUnaVariable)
                    
        return listBlocks
