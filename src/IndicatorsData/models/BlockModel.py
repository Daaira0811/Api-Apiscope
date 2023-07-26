class Block():
    def __init__(self,id,cod_colores=None,lat=None,long=None) -> None:
        self.id=id
        self.cod_colores=cod_colores
        self.lat=lat
        self.long=long

    def to_JSON(self):
        return {
                'id':self.id,
               'cod_colores': self.cod_colores,
               'lat': self.lat,
               'long': self.long
               }
