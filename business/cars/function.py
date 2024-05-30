from .database import CarsDatabase

def get_cars():
    cars = CarsDatabase.get_cars()

    for car in cars:

        fixed_error = car.license_plate

        fixed_error = fixed_error.replace("ERROR_FORBIDDEN", "PATENTE NO DISPONIBLE")

        car.license_plate = fixed_error

    return cars
