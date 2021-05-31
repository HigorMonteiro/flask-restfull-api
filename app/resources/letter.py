import logging

from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource, reqparse, marshal
from flask import request
from random import getrandbits

from app.extensions import db
from app.models import Letter, User, UserLetter
from app.schemas import user_fields, letter_fields


class Create(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("send_email", type=str, required=True, help="send_email")
        parser.add_argument("email", type=str, required=True, help="email")
        parser.add_argument("name", type=str, required=True, help="name")
        parser.add_argument("message", type=str, required=True, help="message")

        args = parser.parse_args()
        user = User.query.filter_by(email=args.send_email).first()

        if not user:
            return {"error": "we don't have that email emailed"}, 400

        try:
            letter = Letter()
            letter.reference_id = f"zappts-{getrandbits(8)}"
            letter.send_email = args.send_email
            letter.email = args.email
            letter.name = args.name
            letter.message = args.message
            letter.user_id = user.id
            db.session.add(letter)
            db.session.commit()

            user_letter = UserLetter()
            user_letter.user = user
            user_letter.letter = letter
            user_letter.user_id = user.id
            user_letter.letter_id = letter.id
            db.session.add(user_letter)
            db.session.commit()

            return marshal(letter, letter_fields, "letter")
        except Exception as e:
            logging.critical(str(e))
            db.session.rollback()
            return {"error": "It was not possible to send your letter"}, 500
