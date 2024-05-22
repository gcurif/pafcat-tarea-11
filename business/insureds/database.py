from common.db_conn import database
from .model import CarModel

"""
Clase que se encarga de manejar la conexión con la base de datos y realizar las consultas necesarias
en particular para la colección de car_model
"""

# Se llama a la collection de car_model de base datos
collection = database['car_model']

class CarModelsDatabase:

    @staticmethod
    def get_car_models():
        db_query_result = collection.find({})
        dict_items = list(db_query_result)

        # Se transforma el diccionario en un Objeto CarModel
        return [CarModel(id=item["_id"], company=item["company"], brand_id=item["brand_id"], model_id=item["model_id"], name=item["name"]  ) for item in dict_items]

