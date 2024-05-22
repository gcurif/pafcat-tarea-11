from common.db_conn import database
from .model import CarType

"""
Clase que se encarga de manejar la conexión con la base de datos y realizar las consultas necesarias
en particular para la colección de car_type
"""

# Se llama a la colección de car_type de la base de datos
collection = database['car_type']

class CarTypesDatabase:

    @staticmethod
    def get_car_types():
        db_query_result = collection.find({})
        dict_items = list(db_query_result)

        # Se transforma el diccionario en un objeto CarType
        return [CarType(id=item["_id"], name=item["name"]) for item in dict_items]
