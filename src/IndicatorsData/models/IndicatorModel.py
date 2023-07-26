class Indicator():
    def __init__(self,id_indicator,nombre=None) -> None:
        self.id=id_indicator
        self.nombre=nombre

    def to_JSON(self):
        return {
                'id':self.id,
               'nombre': self.nombre
               }
