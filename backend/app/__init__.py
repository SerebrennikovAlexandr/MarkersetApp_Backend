from flask import Flask
from .resources import create_api
from config import Config
from app.database import db, migrate
from flask_jwt_extended import JWTManager
from app.mail import mail


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    api = create_api(app)

    jwt = JWTManager(app)

    mail.init_app(app)

    return app
