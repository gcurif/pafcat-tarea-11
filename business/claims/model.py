from datetime import datetime
from pydantic import BaseModel

"""
Clase de Pydantic que define el modelo correspondiente a un json como el siguiente:
{
    "incident_date":"26.09.2018 01:00:00",
    "item":"1",
    "claim_number":"1622861",
    "policy_number":"6536272"
}

Instanciar con Claim(incident_date=datetime.strptime("26.09.2018 01:00:00", "%d.%m.%Y %H:%M:%S"), item="1", claim_number="1622861", policy_number="6536272")
"""
class Claim(BaseModel):
     incident_date: datetime
     item: str
     claim_number: str
     policy_number: str
     