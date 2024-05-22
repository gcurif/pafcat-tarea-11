from common.db_conn import database
from .model import CarBrand

collection = database['car_brand']

class CarBrandsDatabase:
    @staticmethod
    def get_car_brands():
        db_query_result = collection.find({})
        dict_items = list(db_query_result)

        print('dict_items', dict_items)
        return [CarBrand(id=item["_id"], company=item["company"], name=item["name"]  ) for item in dict_items]