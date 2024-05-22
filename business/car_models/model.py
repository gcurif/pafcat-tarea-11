from pydantic import BaseModel

"""
Clase de Pydantic que define el modelo correspondiente a un json como el siguiente:
{
    "company":2,
    "brand_id":851,
    "model_id":1,
    "name":"un modelo"
}
"""
class CarModel(BaseModel):
     company: int
     brand_id: int
     model_id: int
     name: str
     id: int
