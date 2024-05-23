from .database import CarBrandsDatabase

def get_car_brands():

    """
    Lo que se recibe de la base de datos es una lista de vehículos,
    vale decir una lista de objetos CarBrands
    """
    car_brands = CarBrandsDatabase.get_car_brands()

    """
    Se hace un forin para recorrer la lista de marcas
    notar la diferencia entre el car_brand y el car_brands
    singluar y plural, uno para el objeto y otro para la lista
    """
    for car_brand in car_brands:

        """
        El nombre de la marca tiene los siguientes problemas:
        1- No está capitalizado, osea, esta todo en mayudculas
        2- Tiene espacios en blanco al final y al inicio del nombre

        A continuación vamos a corregir el nombre
        """

        # se toma el nombre de la marc y se guarda en la variable fixed_name
        fixed_name = car_brand.name

        # se le quitan los espacios en blanco al inicio y al final
        fixed_name = fixed_name.strip()

        # se capitaliza el nombre
        fixed_name = fixed_name.capitalize()

        # se guarda el nombre corregido en el objeto car_brand
        car_brand.name = fixed_name


        car_brand.name = car_brand.name.capitalize()

    return car_brands
