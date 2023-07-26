class Variable():
    def __init__(self,id_bloque,valor=None, radio=None) -> None:
        self.id=id_bloque
        self.valor=valor
        self.radio=radio

    def to_JSON(self):
        return {
                'id':self.id,
               'valor': self.valor,
               'radio':self.radio

               }
