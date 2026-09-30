from flask import Flask, jsonify
from flask_jwt_extended import JWTManager

from db import db
from routes.user_routes import user_bp
from routes.formulario_routes import formulario_bp

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///banco.db"
app.config["JWT_SECRET_KEY"] = "troque-esta-chave-por-uma-secreta"

db.init_app(app)
jwt = JWTManager(app)

# Registra as rotas
app.register_blueprint(user_bp)
app.register_blueprint(formulario_bp)


# Respostas para erros de token (teste "sem autenticação")
@jwt.unauthorized_loader
def token_ausente(motivo):
    return jsonify({"erro": "Token não enviado. Faça login e envie o Bearer Token."}), 401


@jwt.invalid_token_loader
def token_invalido(motivo):
    return jsonify({"erro": "Token inválido"}), 401


@jwt.expired_token_loader
def token_expirado(header, payload):
    return jsonify({"erro": "Token expirado. Faça login novamente."}), 401


if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # cria as tabelas se ainda não existirem
    app.run(debug=True)
