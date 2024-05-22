from common.db_conn import database
from .model import Car

"""
Clase que se encarga de manejar la conexión con la base de datos y realizar las consultas necesarias
en particular para la colección de car
"""

# Se llama a la collection de car de base datos
collection = database['car']

class CarsDatabase:

    @staticmethod
    def get_cars():
        db_query_result = collection.find({})
        dict_items = list(db_query_result)

        # Se transforma el diccionario en un Objeto Car
        
        return [Car(id=item["_id"], license_plate=item["license_plate"], brand=item["brand"], model=item["model"]) for item in dict_items]