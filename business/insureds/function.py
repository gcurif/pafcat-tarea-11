from .database import InsuredDatabase

def get_insureds():
    insureds = InsuredDatabase.get_insureds()
    for insured in insureds:
        
        fixed_name_insured = insured.name  

        fixed_name_insured = fixed_name_insured.capitalize()

        fixed_name_insured = fixed_name_insured.replace('ï¿½', 'ñ')

        fixed_name_insured = fixed_name_insured.strip()

        insured.name = fixed_name_insured

        #______________________________________________________________

        fixed_full_name = insured.full_name

        fixed_full_name = insured.lastname + insured.lastname2 + insured.mothers_lastname 

        fixed_full_name = fixed_full_name.capitalize()

        fixed_full_name = fixed_full_name.replace('ï¿½', 'ñ')

        fixed_full_name = fixed_full_name.strip()

        insured.full_name = fixed_full_name

    return insureds

    