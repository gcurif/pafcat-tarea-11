from pydantic import BaseModel

"""
Clase de Pydantic que define el modelo correspondiente a un json como el siguiente:
{
    "id": 0,
    "name": "Sin Descripcion"
}
"""
class CarType(BaseModel):
     id: int
     name: str
