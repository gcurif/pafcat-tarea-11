from common.db_conn import database
from .model import Claim

"""
Clase que se encarga de manejar la conexión con la base de datos y realizar las consultas necesarias
en particular para la colección de claim
"""

# Se llama a la collection de claim de base datos
claim_collection = database['claim']

class ClaimsDatabase:

    @staticmethod
    def get_claims():
        db_query_result = claim_collection.find({})
        dict_items = list(db_query_result)

        # Se transforma el diccionario en un Objeto Claim
        return [Claim(id=item["_id"], incident_date=item["incident_date"], item=item["item"], claim_number=item["claim_number"], policy_number=item["policy_number"]) for item in dict_items]