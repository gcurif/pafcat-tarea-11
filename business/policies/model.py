from datetime import datetime
from pydantic import BaseModel, Field, field_validator


"""
Clase de Pydantic que define el modelo correspondiente a un json como el siguiente:

{
	"policy_number" : "6671855",
	"policy_item" : "2",
	"insured" : {
		"identifier" : 763075532
	},
	"office" : {
		"id" : 3573032,
		"name" : "GO SECURITY CORREDORES  DE SEGUROS LTDA"
	},
	"car" : {
		"license_plate" : "JKDC11",
		"year" : 2017,
		"brand_id" : 43,
		"brand_name" : "FREIGHTLINER",
		"model_id" : 14,
		"model_name" : "CASC",
		"motor_serial_number" : "471928S0454130",
		"chassis" : "3AKJGHDV2HSJF7942",
		"type_id" : "P",
		"use_type" : "2",
		"class_type" : "21",
		"model_key" : "CASC 125"
	},
	"status" : "0",
	"start_date" : ISODate("2017-02-16T21:02:00.000-03:00"),
	"end_date" : ISODate("2019-02-16T21:02:00.000-03:00"),
	"risk_number" : "2",
	"product_number" : "760",
	"policy_holder" : {
		"identifier" : 788744404,
		"name" : " TRANSPORTES BOLIVAR LIMITADA",
		"mothers_lastname" : "",
		"lastname" : "TRANSPORTES BOLIVAR LIMITADA"
	},
	"policy_holder_person_sequence" : "539328"
}

"""


class PolicyInsured(BaseModel):
    identifier: str = Field(..., alias="identifier")

class Office(BaseModel):
    id: int = Field(..., alias="id")
    name: str = Field(..., alias="name")


class PolicyCar(BaseModel):
    license_plate: str = Field(..., alias="license_plate")
    year: int = Field(..., alias="year")
    brand_id: int = Field(..., alias="brand_id")
    brand_name: str = Field(..., alias="brand_name")
    model_id: int = Field(..., alias="model_id")
    model_name_desc: str = Field(..., alias="model_name")
    motor_serial_number: str = Field(..., alias="motor_serial_number")
    chassis: str = Field(..., alias="chassis")
    type_id: str = Field(..., alias="type_id")
    use_type: str = Field(..., alias="use_type")
    class_type: str = Field(..., alias="class_type")
    model_key: str = Field(..., alias="model_key")


class PolicyHolder(BaseModel):
    identifier: str = Field(..., alias="identifier")
    name: str = Field(..., alias="name")
    mothers_lastname: str = Field(..., alias="mothers_lastname")
    lastname: str = Field(..., alias="lastname")

class Policy(BaseModel):
    policy_number: str = Field(..., alias="policy_number")
    policy_item: str = Field(..., alias="policy_item")
    insured: PolicyInsured = Field(..., alias="insured")
    office: Office = Field(..., alias="office")
    car: PolicyCar = Field(..., alias="car")
    policy_holder_full_name: str = Field(..., alias="policy_holder_full_name")
    status: int = Field(..., alias="status")
    start_date: datetime = Field(..., alias="start_date")
    end_date: datetime = Field(..., alias="end_date")
    risk_number: str = Field(..., alias="risk_number")
    product_number: str = Field(..., alias="product_number")
    policy_holder: PolicyHolder = Field(..., alias="policy_holder")
    policy_holder_person_sequence: str = Field(..., alias="policy_holder_person_sequence")
	
	
    class config:
        extra = "allow"
