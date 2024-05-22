from pydantic import BaseModel


"""
Clase de pydantic que define el modelo correspondiente a un json como el siguiente:
{
   "company":"2",
   "id":851,
   "name":"."
}
"""
class CarBrand(BaseModel):
    company: int
    id: int
    name: str