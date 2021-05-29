import logging

from app.extensions import db
from app.models import User
from flask_restful import Resource, reqparse
from werkzeug.security import generate_password_hash


class Login(Resource):
    def get(self):
        return "login"


class Register(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("email", required=True, help="O campo email é obrigatório")
        parser.add_argument(
            "password", required=True, help="O campo senha é obrigatório"
        )
        args = parser.parse_args()

        user = User.query.filter_by(email=args.email).first()
        if user:
            return {"error": "e-mail já registrado!"}, 400

        user = User()
        user.email = args.email
        user.password = generate_password_hash(args.password)

        db.session.add(user)
        try:
            db.session.commit()
            return {"message": "Usuario registrado com sucesso"}, 201
        except Exception as e:
            db.session.rollback()
            logging.critical(str(e))
            return {"error": "nao foi possivel registrar o usuario"}, 500
