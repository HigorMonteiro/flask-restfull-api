from flask_restful import Api

from app.resources import auth, letter


def init_app(app):
    api = Api(app, prefix="/api")
    api.add_resource(auth.Login, "/auth/login")
    api.add_resource(auth.Register, "/auth/register")
    api.add_resource(auth.ForgetPassword, "/auth/forget-password")

    api.add_resource(letter.Create, "/letter/create")
    api.add_resource(letter.LetterList, "/letters")
    api.add_resource(letter.LetterGet, "/letters/<reference_id>")
