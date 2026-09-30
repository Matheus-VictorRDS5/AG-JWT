from flask import request, jsonify
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash, check_password_hash

from db import db
from models.user_model import User


def cadastrar_usuario():
    dados = request.get_json() or {}
    nome = dados.get("nome")
    email = dados.get("email")
    senha = dados.get("senha")

    if not nome or not email or not senha:
        return jsonify({"erro": "nome, email e senha são obrigatórios"}), 400

    if User.query.filter_by(email=email).first():
        return jsonify({"erro": "Email já cadastrado"}), 409

    usuario = User(nome=nome, email=email, senha_hash=generate_password_hash(senha))
    db.session.add(usuario)
    db.session.commit()
    return jsonify({"mensagem": "Usuário cadastrado com sucesso", "usuario": usuario.to_dict()}), 201


def login():
    dados = request.get_json() or {}
    usuario = User.query.filter_by(email=dados.get("email")).first()

    if not usuario or not check_password_hash(usuario.senha_hash, dados.get("senha", "")):
        return jsonify({"erro": "Email ou senha inválidos"}), 401

    # identity precisa ser string nas versões novas do flask-jwt-extended
    token = create_access_token(identity=str(usuario.id))
    return jsonify({"access_token": token}), 200


def consultar_usuario(id):
    usuario = db.session.get(User, id)
    if not usuario:
        return jsonify({"erro": "Usuário não encontrado"}), 404
    return jsonify(usuario.to_dict()), 200


def atualizar_usuario(id):
    usuario = db.session.get(User, id)
    if not usuario:
        return jsonify({"erro": "Usuário não encontrado"}), 404

    dados = request.get_json() or {}

    # Só atualiza os campos permitidos que foram enviados
    if "nome" in dados:
        usuario.nome = dados["nome"]
    if "email" in dados:
        outro = User.query.filter_by(email=dados["email"]).first()
        if outro and outro.id != usuario.id:
            return jsonify({"erro": "Email já está em uso"}), 409
        usuario.email = dados["email"]
    if "senha" in dados:
        usuario.senha_hash = generate_password_hash(dados["senha"])

    db.session.commit()
    return jsonify({"mensagem": "Usuário atualizado com sucesso", "usuario": usuario.to_dict()}), 200


def excluir_usuario(id):
    usuario = db.session.get(User, id)
    if not usuario:
        return jsonify({"erro": "Usuário não encontrado"}), 404

    db.session.delete(usuario)
    db.session.commit()
    return jsonify({"mensagem": "Usuário excluído com sucesso"}), 200
