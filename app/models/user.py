from app.services.json_handler import read_json, write_json
from app.services.user_service import check_if_email_already_in_users, transforming_email_in_lower_case, transforming_fist_letter_in_upper_case
from app.exceptions.already_exist_this_email import AlreadyExistThisEmailError

class User:

    FILEPATH = "app/database/database.json"


    def __init__(self, email: str, name: str) -> None:
        self.email = email
        self.name = name


    @classmethod
    def get_user(cls) -> list[dict]:
        return read_json(cls.FILEPATH)


    def save_new_user(self):

        user = self.__dict__
        user["email"] = transforming_email_in_lower_case(self.email)
        user["name"] = transforming_fist_letter_in_upper_case(self.name)
        user["id"] = len(read_json(self.FILEPATH)) + 1

        if check_if_email_already_in_users(self.FILEPATH, user["email"]):
            raise AlreadyExistThisEmailError

        if type(self.email) != str or type(self.name) != str:
            raise TypeError

        return write_json(self.FILEPATH, user)


                


