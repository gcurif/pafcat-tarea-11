# import clases de mongo engine 
from mongoengine import Document, StringField

"""
Clase de mongoengine que define el modelo correspondiente a un json como el siguiente:
{
   "company":"2",
   "brand_id":"851",
   "model_id":"1",
   "name":"."
}
"""
class CarModel(Document):
    company = StringField()
    brand_id = StringField()
    model_id = StringField()
    name = StringField()

    @staticmethod
    def from_json(json):
        return CarModel(company=json['company'], brand_id=json['brandId'], model_id=json['modelId'], name=json['name'])
    
    def __str__(self):
        return f"CarModel(company={self.company}, brand_id={self.brand_id}, model_id={self.model_id}, name={self.name})"
