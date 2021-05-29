from flask import Flask
from dynaconf import FlaskDynaconf
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_migrate import Migrate

db = SQLAlchemy()


def init_app(app):
    FlaskDynaconf(app)
    JWTManager(app)
    CORS(app)

    db.init_app(app)
    Migrate(app)
