from .database import InsuredDatabase

def get_insureds():
    insureds = InsuredDatabase.get_insureds()
    for insured in insureds:
        
        fixed_name_insured = insured.name  

        fixed_name_insured = fixed_name_insured.capitalize()

        fixed_name_insured = fixed_name_insured.replace('ï¿½', 'ñ')

        fixed_name_insured = fixed_name_insured.strip()

        insured.name = fixed_name_insured

    return insureds

    