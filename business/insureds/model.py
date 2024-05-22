# import clases de mongo engine 
from mongoengine import Document, EmbeddedDocument, StringField, IntField, EmbeddedDocumentField

"""
Clase de mongoengine que define el modelo correspondiente a un json como el siguiente:
{
  "identifier": 123456,
  "name": "John",
  "lastname": "Doe",
  "mothers_lastname": "Smith",
  "lastname2": "Brown",
  "persontype": "Individual",
  "sperson": "No",
  "contact_data": {
    "phone1": "555-1234",
    "phone2": "555-5678",
    "email": "john.doe@example.com"
  },
  "address": {
    "region": {
      "id": 1,
      "name": "West Coast"
    },
    "city": {
      "id": 2,
      "name": "Los Angeles"
    },
    "district": {
      "id": 3,
      "name": "Central LA"
    },
    "streetnumber": "1234",
    "street": "Boulevard St"
  }
}
"""
class Region(EmbeddedDocument):
    id = IntField(primary_key=True)
    name = StringField()

    def __str__(self):
        return f"Region(id={self.id}, name={self.name})"

class City(EmbeddedDocument):
    id = IntField(primary_key=True)
    name = StringField()

    def __str__(self):
        return f"City(id={self.id}, name={self.name})" 

class District(EmbeddedDocument):
    id = IntField(primary_key=True)
    name = StringField()

    def __str__(self):
        return f"District(id={self.id}, name={self.name})"

class Address(EmbeddedDocument):
    region = EmbeddedDocumentField(Region)
    city = EmbeddedDocumentField(City)
    district = EmbeddedDocumentField(District)
    streetnumber = StringField()
    street = StringField()

    def __str__(self):
        return f"Address(region={self.region}, city={self.city}, district={self.district}, streetnumber={self.streetnumber}, street={self.street})"

class ContactData(EmbeddedDocument):
    phone1 = StringField()
    phone2 = StringField()
    email = StringField()

    def __str__(self):
        return f"ContactData(phone1={self.phone1}, phone2={self.phone2}, email={self.email})"

class Insured(Document):
    identifier = IntField()
    name = StringField()
    lastname = StringField()
    mothers_lastname = StringField()
    lastname2 = StringField()
    persontype = StringField()
    sperson = StringField()
    contact_data = EmbeddedDocumentField(ContactData)
    address = EmbeddedDocumentField(Address)

    @staticmethod
    def from_json(json_data):
        # Crear las instancias de Region, City, y District
        region_instance = Region(id=json_data['address']['region']['id'], name=json_data['address']['region']['name'])
        city_instance = City(id=json_data['address']['city']['id'], name=json_data['address']['city']['name'])
        district_instance = District(id=json_data['address']['district']['id'], name=json_data['address']['district']['name'])
        
        # Crear la instancia de Address con las instancias de Region, City y District
        address_instance = Address(
            region=region_instance,
            city=city_instance,
            district=district_instance,
            streetnumber=json_data['address']['streetnumber'],
            street=json_data['address']['street']
        )
        
        # Crear la instancia de ContactData
        contact_data_instance = ContactData(
            phone1=json_data['contact_data']['phone1'],
            phone2=json_data['contact_data']['phone2'],
            email=json_data['contact_data']['email']
        )
        
        # Crear la instancia final de Insured con todas las subinstancias
        insured_instance = Insured(
            identifier=json_data['identifier'],
            name=json_data['name'],
            lastname=json_data['lastname'],
            mothers_lastname=json_data['mothers_lastname'],
            lastname2=json_data['lastname2'],
            persontype=json_data['persontype'],
            sperson=json_data['sperson'],
            contact_data=contact_data_instance,
            address=address_instance
        )
        
        return insured_instance
    
    def __str__(self):
        return f"Insured(identifier={self.identifier}, name={self.name}, lastname={self.lastname}, mothers_lastname={self.mothers_lastname}, lastname2={self.lastname2}, persontype={self.persontype}, sperson={self.sperson}, contact_data={self.contact_data}, address={self.address})"

