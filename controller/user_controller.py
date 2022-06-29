from flask import Blueprint, request, jsonify
from service.dao.user_dao import user_schema
import service.user_service as user_service


user = Blueprint("user", __name__)

"""
- Metodo que permite validar las credenciales de autenticacion de usuario contra la tabla users
- Params: datos de autenticacion, usuario tipo string y password tipo string
- Return objeto json del usuario si las credenciales son validas, vacio en caso contrario 
"""


@user.route("/login", methods=["POST"])
def login():

    request_data = request.get_json()
    username = request_data["username"]
    password = request_data["password"]
    user = user_service.login(username, password)

    if user:
        user.password = "*****"

    return user_schema.dump(user)
