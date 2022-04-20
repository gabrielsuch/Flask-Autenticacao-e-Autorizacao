from flask import Flask
from app import routes
from app.configs import database, migration, jwt


def create_app():
    app = Flask(__name__)

    routes.init_app(app)
    database.init_app(app)
    migration.init_app(app)
    jwt.init_app(app)

    return app