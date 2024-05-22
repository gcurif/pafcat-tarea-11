from .database import InsuredDatabase

def get_insureds():
    insureds = InsuredDatabase.get_insureds()
    return insureds

