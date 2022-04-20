from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import os


db = SQLAlchemy()


def init_app(app: Flask):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JSON_SORT_KEYS"] = False

    db.init_app(app)

    app.db = db

    from app.models.user_model import UserModel