# import clases de mongo engine 
from mongoengine import Document, EmbeddedDocument, StringField, IntField, EmbeddedDocumentField, DateTimeField
from datetime import datetime

"""
Clase de mongoengine que define el modelo correspondiente a un json como el siguiente:
{
   "policy_number":"6136115",
   "policy_item":"0",
   "insured":{
      "identifier":"81201000K"
   },
   "office":{
      "id":8204024,
      "name":"CAT CORREDORES DE SEGUROS Y SERVICIOS S.A."
   },
   "car":{
      "license_plate":"",
      "year":2008,
      "brand_id":"14",
      "brand_name":"CHEVROLET",
      "model_id":"125",
      "model_name":"CORSA",
      "motor_serial_number":"",
      "chassis":"",
      "type_id":"L",
      "use_type":"1",
      "class_type":"1",
      "modelkey":"CORSA EXTRA ML 1.6 PWR CD"
   },
   "status":"0",
   "start_date":"15/01/2011 00:01:00",
   "end_date":"30/06/2020 00:06:00",
   "risk_number":"1",
   "product_number":"410",
   "policy_holder":{
      "identifier":"81201000K",
      "name":" CENCOSUD RETAIL S.A.",
      "mothers_lastname":"",
      "lastname":"CENCOSUD RETAIL S.A."
   },
   "policy_holder_person_sequence":"354341"
}
"""
class PolicyInsured(EmbeddedDocument):
    identifier = StringField()

    def __str__(self):
        return f"PolicyInsured(identifier={self.identifier})"

class Office(EmbeddedDocument):
    id = IntField()
    name = StringField()

    def __str__(self):
        return f"Office(id={self.id}, name={self.name})"

class PolicyCar(EmbeddedDocument):
    license_plate = StringField()
    year = IntField()
    brand_id = StringField()
    brand_name = StringField()
    model_id = StringField()
    model_name = StringField()
    motor_serial_number = StringField()
    chassis = StringField()
    type_id = StringField()
    use_type = StringField()
    class_type = StringField()  # Use class_ to avoid conflict with Python's reserved word 'class'
    model_key = StringField()

    def __str__(self):
        return f"PolicyCar(license_plate={self.license_plate}, year={self.year}, brand_id={self.brand_id}, brand_name={self.brand_name}, model_id={self.model_id}, model_name={self.model_name}, motor_serial_number={self.motor_serial_number}, chassis={self.chassis}, type_id={self.type_id}, use_type={self.use_type}, class_type={self.class_type}, model_key={self.model_key})"

class PolicyHolder(EmbeddedDocument):
    identifier = StringField()
    name = StringField()
    mothers_lastname = StringField()
    lastname = StringField()

    def __str__(self):
        return f"PolicyHolder(identifier={self.identifier}, name={self.name}, mothers_lastname={self.mothers_lastname}, lastname={self.lastname})"

class Policy(Document):
    policy_number = StringField()
    policy_item = StringField()
    insured = EmbeddedDocumentField(PolicyInsured)
    office = EmbeddedDocumentField(Office)
    car = EmbeddedDocumentField(PolicyCar)
    status = StringField()
    start_date = DateTimeField()
    end_date = DateTimeField()
    risk_number = StringField()
    product_number = StringField()
    policy_holder = EmbeddedDocumentField(PolicyHolder)
    policy_holder_person_sequence = StringField()

    @staticmethod
    def from_json(json_data):
        return Policy(
            policy_number=json_data['policynumber'],
            policy_item=json_data['policyitem'],
            insured=PolicyInsured(**json_data['insured']),
            office=Office(**json_data['office']),
            car=PolicyCar(**json_data['car']),
            status=json_data['status'],
            start_date=datetime.strptime(json_data['startDate'], "%d/%m/%Y %H:%M:%S"),
            end_date=datetime.strptime(json_data['endDate'], "%d/%m/%Y %H:%M:%S"),
            risk_number=json_data['risknumber'],
            product_number=json_data['productnumber'],
            policy_holder=PolicyHolder(**json_data['policyholder']),
            policy_holder_person_sequence=json_data['policyholderpersonsequence']
        )
    
    def __str__(self):
        return f"Policy(policy_number={self.policy_number}, policy_item={self.policy_item}, insured={self.insured}, office={self.office}, car={self.car}, status={self.status}, start_date={self.start_date}, end_date={self.end_date}, risk_number={self.risk_number}, product_number={self.product_number}, policy_holder={self.policy_holder}, policy_holder_person_sequence={self.policy_holder_person_sequence})"

