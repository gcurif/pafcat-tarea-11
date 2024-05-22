from .database import ClaimsDatabase

def get_claims():
    claims = ClaimsDatabase.get_claims()
    return claims
