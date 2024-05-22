from pydantic import BaseModel

"""
Clase de Pydantic que define el modelo correspondiente a un json como el siguiente:
{
    "license_plate": "fcrt78",
	"brand" : {
		"id" : 62,
		"name" : "TOYOTA"
	},
	"model" : {
		"id" : 103,
		"name" : "COROLLA                                 "
	}
}
Instanciar con Car(license_plate="fcrt78", brand="toyota", model="rav4")
"""
class CarBrand(BaseModel):
    id: int
    name: str

class CarModel(BaseModel):
    id: int
    name: str

class Car(BaseModel):
    license_plate: str
    brand: CarBrand
    model: CarModel
