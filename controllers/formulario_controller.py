from flask import request, jsonify

from db import db
from models.formulario_model import Formulario


def cadastrar_formulario():
    dados = request.get_json() or {}
    titulo = dados.get("titulo")
    descricao = dados.get("descricao")

    if not titulo or not descricao:
        return jsonify({"erro": "titulo e descricao são obrigatórios"}), 400

    formulario = Formulario(titulo=titulo, descricao=descricao)
    db.session.add(formulario)
    db.session.commit()
    return jsonify({"mensagem": "Formulário cadastrado com sucesso", "formulario": formulario.to_dict()}), 201


def consultar_formulario(id):
    formulario = db.session.get(Formulario, id)
    if not formulario:
        return jsonify({"erro": "Formulário não encontrado"}), 404
    return jsonify(formulario.to_dict()), 200


def atualizar_formulario(id):
    formulario = db.session.get(Formulario, id)
    if not formulario:
        return jsonify({"erro": "Formulário não encontrado"}), 404

    dados = request.get_json() or {}
    if "titulo" in dados:
        formulario.titulo = dados["titulo"]
    if "descricao" in dados:
        formulario.descricao = dados["descricao"]

    db.session.commit()
    return jsonify({"mensagem": "Formulário atualizado com sucesso", "formulario": formulario.to_dict()}), 200


def excluir_formulario(id):
    formulario = db.session.get(Formulario, id)
    if not formulario:
        return jsonify({"erro": "Formulário não encontrado"}), 404

    db.session.delete(formulario)
    db.session.commit()
    return jsonify({"mensagem": "Formulário excluído com sucesso"}), 200
