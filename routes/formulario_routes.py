from flask import Blueprint
from flask_jwt_extended import jwt_required

from controllers import formulario_controller

formulario_bp = Blueprint("formularios", __name__, url_prefix="/formularios")


# POST /formularios/ -> JWT
@formulario_bp.route("/", methods=["POST"])
@jwt_required()
def cadastrar():
    return formulario_controller.cadastrar_formulario()


# GET /formularios/<id> -> JWT
@formulario_bp.route("/<int:id>", methods=["GET"])
@jwt_required()
def consultar(id):
    return formulario_controller.consultar_formulario(id)


# PUT /formularios/<id> -> JWT
@formulario_bp.route("/<int:id>", methods=["PUT"])
@jwt_required()
def atualizar(id):
    return formulario_controller.atualizar_formulario(id)


# DELETE /formularios/<id> -> JWT
@formulario_bp.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def excluir(id):
    return formulario_controller.excluir_formulario(id)
