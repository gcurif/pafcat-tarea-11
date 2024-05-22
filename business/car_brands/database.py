from common.db_conn import database
from .model import CarBrand

"""
Clase que se encarga de manejar la conexión con la base de datos y realizar las consultas necesarias
en particular para la colección de car_brands
"""

# Se llama a la collection de car_brand de base datos
collection = database['car_brand']

class CarBrandsDatabase:

    @staticmethod
    def get_car_brands():
        db_query_result = collection.find({})
        dict_items = list(db_query_result)

        # Se transforma el diccionario en un Objeto Carbrand
        return [CarBrand(id=item["_id"], company=item["company"], name=item["name"]  ) for item in dict_items]

