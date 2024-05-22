from .database import CarsDatabase

def get_cars():
    cars = CarsDatabase.get_cars()
    return cars
