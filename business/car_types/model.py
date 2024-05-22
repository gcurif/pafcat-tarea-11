# import clases de mongo engine 
from mongoengine import Document, StringField, IntField

"""
Clase de mongoengine que define el modelo correspondiente a un json como el siguiente:
{
   "id":0,
   "name":"Sin Descripcion"
}
"""
class CarType(Document):
    id = IntField(primary_key=True)
    name = StringField()

    @staticmethod
    def from_json(json):
        return CarType(id=json['id'], name=json['name'])
    def __str__(self):
        return f"CarType(id={self.id}, name={self.name})"
