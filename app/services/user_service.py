from lib2to3.pytree import type_repr
from app.services.json_handler import read_json


def transforming_email_in_lower_case(email: str):
    
    return email.lower() if type(email) is str else email


def transforming_fist_letter_in_upper_case(name: str):

    new_name = ""
        
    if name is str:
        name = name.split(" ")

        for index, word in enumerate(name):
            new_name += f"{word.capitalize()} " if len(name)-1 > index else word.capitalize()

    return new_name if type(name) is str else name


def check_if_email_already_in_users(filepath: str, email: str):

    users_list = read_json(filepath)

    for user in users_list:

        if user["email"] == email:
            
            return True

    return False


def check_if_type_values(key: str):

    type_value = type(key)

    if type_value is int:
        return "Integer"

    elif type_value is float:
        return "Float" 

    elif type_value is list:
        return "List"

    elif type_value is dict:
        return "Dictionary"

    elif type_value is bool:
        return "Boolean"               


def check_if_type_values_in_dict_are_strings(email: str, name: str):

    email_type = type(email)    
    name_type = type(name)    

    if email_type is not str and name_type is str:
        return {"wrong fields": [
            {
                "email": check_if_type_values(email)
            }
        ]}

    elif email_type is str and name_type is not str:
         return {"wrong fields": [
            {
                "name": check_if_type_values(name)
            }
        ]}

    else:
        return {"wrong fields": [
            {
                "email": check_if_type_values(email)
            },
             {
                "name": check_if_type_values(name)
            }
        ]}  


