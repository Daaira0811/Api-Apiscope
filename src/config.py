
from decouple import config

class Config:
    SECRET_KEY=config('SECRET_KEY')

# Se asigna la configuración de desarrollo y se establece en DEBUG para que el servidor se refresque sólo al 
# realiza cualquier cambio
class DevelopmentConfig(Config):
    DEBUG= True

config={
    'development' : DevelopmentConfig
}