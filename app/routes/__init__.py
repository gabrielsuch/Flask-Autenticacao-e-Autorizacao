from flask import Flask
from app.routes.user_route import bp


def init_app(app: Flask):
    app.register_blueprint(bp)
    