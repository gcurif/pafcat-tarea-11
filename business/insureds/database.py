from common.db_conn import database
from .model import Insured
import re
"""
Clase que se encarga de manejar la conexión con la base de datos y realizar las consultas necesarias
en particular para la colección de insuredes
"""

# Se llama a la collection de insuredes de base datos
collection = database['insured']




class InsuredDatabase:

    @staticmethod
    def get_insureds():
        db_query_result = collection.find({})
        dict_items = list(db_query_result)

        for item in dict_items:
            item["address"]["streetnumber"] = re.sub(r"\D", "", item["address"]["street"])
            if item["address"]["streetnumber"] == "":
                item["address"]["streetnumber"] = None
            else:
                 item["address"]["streetnumber"] = int(item["address"]["streetnumber"])
            item["identifier"] = str(item["identifier"])
            item["identifier"] = str(item["identifier"])
            item["full_name"] = item.pop("id", None)     
        # Se transforma el diccionario en un Objeto CarModel
        return [Insured( **item) for item in dict_items]
