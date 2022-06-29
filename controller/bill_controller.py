from flask import Blueprint, request, jsonify
from service.dao.bill_dao import bill_schema, bills_schema
import service.bill_service as bill_service


bill = Blueprint("bill", __name__)

"""
- Metodo que devuelve un bill dado su identificador
- Params: id: identificador del bill
- Return objeto json asociado al id, vacio en caso de no encontrar coicidencias
"""


@bill.route("/bill/<id>")
def get(id):
    bill = bill_service.get(id)
    return bill_schema.dump(bill)


"""
- Metodo que elimina un bill dado su identificador
- Params: id: identificador del bill a ser eliminado
- Return objeto json asociado al registro eliminado, vacio en caso de no encontrar coicidencias
"""


@bill.route("/bill/<id>", methods=["DELETE"])
def delete(id):
    bill = bill_service.delete(id)
    return bill_schema.dump(bill)


"""
- Metodo que devuelve todos los bills registrados en la BD
- Return Lista de objetos json, vacio en caso de no encontrar registros
"""


@bill.route("/bills/<username>")
def list(username):
    bills = bill_service.list(username)
    return jsonify(bills_schema.dump(bills))


"""
- Metodo que registra un nuevo bill
- Params: datos de creacion del bill: user_id, value, type, observation
- Return objeto json del registro creado, vacio en caso de error
"""


@bill.route("/bill", methods=["POST"])
def save():

    request_data = request.get_json()
    user_id = request_data["user_id"]
    value = request_data["value"]
    type = request_data["type"]
    observation = request_data["observation"]

    bill = bill_service.save(user_id, value, type, observation)
    return bill_schema.dump(bill)
