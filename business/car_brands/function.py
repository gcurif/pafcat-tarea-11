from .database import CarBrandsDatabase

def get_car_brands():
    car_brands = CarBrandsDatabase.get_car_brands()
    print('cb', car_brands)
    return car_brands
