# import clases de mongo engine 
from mongoengine import Document, EmbeddedDocument, StringField, IntField, EmbeddedDocumentField, DateTimeField
from datetime import datetime

"""
Clase de mongoengine que define el modelo correspondiente a un json como el siguiente:
{
    "licenseplate": "fcrt78",
    "brand": "toyota"
    "model": "rav4"
}
"""
class Car(Document):
    license_plate = StringField()
    brand = StringField()
    model = StringField()

    @staticmethod
    def from_json(json):
        return Car(license_plate=json['licenseplate'], brand=json['brand'], model=json['model'])
    
    def __str__(self):
        return f"Car(license_plate={self.license_plate}, brand={self.brand}, model={self.model})"
