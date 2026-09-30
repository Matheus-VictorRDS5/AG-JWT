from db import db


class Formulario(db.Model):
    __tablename__ = "formularios"

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(150), nullable=False)
    descricao = db.Column(db.Text, nullable=False)

    def to_dict(self):
        return {"id": self.id, "titulo": self.titulo, "descricao": self.descricao}
