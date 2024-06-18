from .database import CarTypesDatabase

def get_car_types():
    car_types = CarTypesDatabase.get_car_types()

    for car_type in car_types:

            fixed_name_type = car_type.name

            fixed_name_type =  fixed_name_type.strip()

            fixed_name_type = fixed_name_type.capitalize()

            fixed_name_type = fixed_name_type.replace('ï¿½', 'ñ')

            car_type.name = fixed_name_type

    return car_types
