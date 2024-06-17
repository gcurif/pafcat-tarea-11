from pydantic import BaseModel, Field
from typing import Optional
"""
Clase de Pydantic que define el modelo correspondiente a un json como el siguiente:
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
class Region(BaseModel):
    id: int = Field(..., alias="_id")
    name: str

class City(BaseModel):
    id: int = Field(..., alias="_id")
    name: str

class District(BaseModel):
    id: int = Field(..., alias="_id")
    name: str

class Address(BaseModel):
    region: Region
    city: City
    district: District
    streetnumber: Optional[int] = None  
    street: str

class ContactData(BaseModel):
    phone1: str
    phone2: str
    email: str

class Insured(BaseModel):
    identifier: str
    name: str
    lastname: str
    mothers_lastname: str
    lastname2: str
    persontype: str
    sperson: str
    contact_data: ContactData
    address: Address
    full_name: None


    