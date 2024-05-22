from common.db_conn import database
from .model import Policy

"""
Clase que se encarga de manejar la conexión con la base de datos y realizar las consultas necesarias
en particular para la colección de políticas
"""

# Se llama a la colección de políticas de la base de datos
policy_collection = database['policy']

class PolicyDatabase:

    @staticmethod
    def get_policies():
        db_query_result = policy_collection.find({})
        dict_items = list(db_query_result)

        return [Policy(**item) for item in dict_items]
        # Se transforma el diccionario en un objeto Policy
