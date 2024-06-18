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

        #______________________________________________________________

        fixed_contact_data_phone1 = insured.contact_data.phone1

        fixed_contact_data_phone1 = fixed_contact_data_phone1.replace('0000000000', 'NO DISPONIBLE')

        insured.contact_data.phone1 = fixed_contact_data_phone1

        #______________________________________________________________


        fixed_contact_data_phone2 = insured.contact_data.phone2

        fixed_contact_data_phone2 = fixed_contact_data_phone2.replace('0000000000', 'NO DISPONIBLE')

        insured.contact_data.phone2 = fixed_contact_data_phone2

        #______________________________________________________________

        fixed_contact_data_email = insured.contact_data.email

        fixed_contact_data_email = fixed_contact_data_email.replace('', 'EMAIL NO DISPONIBLE')

        insured.contact_data.email = fixed_contact_data_email
        
    return insureds

    