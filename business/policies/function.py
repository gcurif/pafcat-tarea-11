from .database import PolicyDatabase
from datetime import datetime

def get_policies():
    claims = PolicyDatabase.get_policies()
    for claim in claims:

        fixedcar_motor_serial_number = claim.car.motor_serial_number

        fixedcar_motor_serial_number = fixedcar_motor_serial_number.replace("s/n", "S/N")

        claim.car.motor_serial_number = fixedcar_motor_serial_number

        #________________________________________________________________

        fixed_car_chassis = claim.car.chassis

        fixed_car_chassis = fixed_car_chassis.replace("s/n", "S/N")

        claim.car.chassis = fixed_car_chassis

        #_________________________________________________________________

        fixed_policy_holder_full_name = claim.policy_holder_full_name

        fixed_policy_holder_full_name = claim.policy_holder.name + claim.policy_holder.lastname

        fixed_policy_holder_full_name = fixed_policy_holder_full_name.capitalize()

        claim.policy_holder.lastname = fixed_policy_holder_full_name

        #_________________________________________________________________

        fixed_office_name = claim.office.name

        fixed_office_name = fixed_office_name.capitalize()

        fixed_office_name = fixed_office_name.replace("S. A", "S.A")

        claim.office.name = fixed_office_name

        #_________________________________________________________________

        
        

        actual_date = datetime.now()
        
        if  claim.end_date < actual_date:
            claim.status = 1

        else:
            claim.status = 0

        

    return claims