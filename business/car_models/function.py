from .database import CarModelsDatabase

def get_car_models():
    car_models = CarModelsDatabase.get_car_models()

    for car_model in car_models:
            
            fixed_name_models = car_model.name

            fixed_name_models = fixed_name_models.capitalize()

            fixed_name_models = fixed_name_models.replace('ï¿½', 'ñ')

            fixed_name_models = fixed_name_models.strip()

            car_model.name = fixed_name_models

    return car_models

