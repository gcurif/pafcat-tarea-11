from .database import CarModelsDatabase

def get_car_models():
    car_models = CarModelsDatabase.get_car_models()


    return car_models

