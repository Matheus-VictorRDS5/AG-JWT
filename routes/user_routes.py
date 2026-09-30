from flask import Blueprint
from flask_jwt_extended import jwt_required

from controllers import user_controller

user_bp = Blueprint("users", __name__, url_prefix="/users")


# POST /users/ -> Cadastro (público)
@user_bp.route("/", methods=["POST"])
def cadastrar():
    return user_controller.cadastrar_usuario()


# POST /users/login -> Login (público)
@user_bp.route("/login", methods=["POST"])
def login():
    return user_controller.login()


# GET /users/<id> -> JWT
@user_bp.route("/<int:id>", methods=["GET"])
@jwt_required()
def consultar(id):
    return user_controller.consultar_usuario(id)


# PUT /users/<id> -> JWT
@user_bp.route("/<int:id>", methods=["PUT"])
@jwt_required()
def atualizar(id):
    return user_controller.atualizar_usuario(id)


# DELETE /users/<id> -> JWT
@user_bp.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def excluir(id):
    return user_controller.excluir_usuario(id)
