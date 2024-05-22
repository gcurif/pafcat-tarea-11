# import clases de mongo engine 
from mongoengine import Document, StringField, DateTimeField
from datetime import datetime

"""
Clase de mongoengine que define el modelo correspondiente a un json como el siguiente:
{
   "incident_date":"26.09.2018 01:00:00",
   "item":"1",
   "claim_number":"1622861",
   "policy_number":"6536272"
}
"""
class Claim(Document):
    incident_date = DateTimeField()
    item = StringField()
    claim_number = StringField()
    policy_number = StringField()

    @staticmethod
    def from_json(json_data):
        return Claim(
            incident_date=datetime.strptime(json_data['incident_date'], "%d.%m.%Y %H:%M:%S"),
            item=json_data['item'],
            claim_number=json_data['claim_number'],
            policy_number=json_data['policy_number']
        )
    
    def __str__(self):
        return f"Claim(incident_date={self.incident_date}, item={self.item}, claim_number={self.claim_number}, policy_number={self.policy_number})"