from .database import PolicyDatabase

def get_policies():
    claims = PolicyDatabase.get_policies()
    return claims
