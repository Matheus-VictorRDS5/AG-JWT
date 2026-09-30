# API Login + Cadastro + CRUD (Flask + JWT)

API com usuários e formulários. As rotas de consulta, alteração e exclusão exigem autenticação JWT.

## Estrutura
- `app.py` – cria o app, configura o JWT e registra as rotas
- `db.py` – objeto do banco (SQLAlchemy)
- `models/` – tabelas (User, Formulario)
- `controllers/` – lógica de cada operação
- `routes/` – rotas (URLs) e proteção com `@jwt_required()`
- `Comandos_Postman.txt` – requisições para teste

## Como rodar
```
pip install flask flask-sqlalchemy flask-jwt-extended
python app.py
```

## Rotas
| Método | Rota | Autenticação |
|---|---|---|
| POST | /users/ | Não (cadastro) |
| POST | /users/login | Não (retorna access_token) |
| GET / PUT / DELETE | /users/<id> | JWT |
| POST | /formularios/ | JWT |
| GET / PUT / DELETE | /formularios/<id> | JWT |
