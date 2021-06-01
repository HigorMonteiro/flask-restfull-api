from pytest import fixture

from app import create_app
from app.extensions import db
from app.models import Letter, User


@fixture
def app():
    app = create_app()
    app.testing = True
    return app

@fixture
def create_database(app):
    with app.app_context():
        db.create_all()
        yield db

        db.session.remove()
        db.drop_all()

@fixture(autouse=True)
def makedb(create_database):

    letter = Letter()
    letter.name = "Higor Vinicius"
    letter.send_email = "higorvmonteiro@gmail.com"
    letter.email = "higor@gmail.com"
    letter.message = "Olá Papai Noel quero um carrinho de controle remoto"
    letter.reference_id = "ZAPPTS-99"
    letter.user_id = 1
    db.session.add(letter)
    db.session.commit()