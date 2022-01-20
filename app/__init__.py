from http import HTTPStatus
from flask import Flask, jsonify, request
from app.exceptions.already_exist_this_email import AlreadyExistThisEmailError

from app.services.json_handler import read_json, write_json
from app.models.user import User
from app.services.user_service import check_if_type_values_in_dict_are_strings

app = Flask(__name__)


@app.get("/user")
def show_users():
    return jsonify(User.get_user()), HTTPStatus.OK


@app.post("/user")
def register_user():

    data = request.get_json()

    user = User(**data)

    try:
        
        return user.save_new_user(), HTTPStatus.CREATED 

    except AlreadyExistThisEmailError:

        return {"msg": "User already exists"}, HTTPStatus.CONFLICT

    except TypeError:

        return check_if_type_values_in_dict_are_strings(data["email"], data["name"]), HTTPStatus.BAD_REQUEST
