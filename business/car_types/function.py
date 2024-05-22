from .database import CarTypesDatabase

def get_car_types():
    car_types = CarTypesDatabase.get_car_types()
    return car_types
