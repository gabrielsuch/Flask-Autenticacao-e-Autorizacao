from flask import request, jsonify, current_app
from app.models.user_model import UserModel
import secrets
from app.configs.auth import auth
from sqlalchemy.exc import IntegrityError


@auth.login_required
def get_users():
    user = auth.current_user()

    return {
        "name": user.name,
        "last_name": user.last_name,
        "email": user.email
    }


def create_account():
    data = request.get_json()

    try:
        data["api_key"] = secrets.token_urlsafe(32)

        password_to_hash = data.pop("password")

        user = UserModel(**data)

        user.password = password_to_hash

        current_app.db.session.add(user)
        current_app.db.session.commit()

        serialized = {
            "name": user.name,
            "last_name": user.last_name,
            "email": user.email
        }

        return jsonify(serialized), 201

    except IntegrityError:
        return {
            "error": "Email already exists!"
        }, 409


def login():
    data = request.get_json()

    user = UserModel.query.filter_by(email = data["email"]).first()

    if(not user or not user.verify_password(data["password"])):
        return {
            "error": "Email or Password doesn't matches"
        }, 404

    return {
        "api_key": user.api_key
    }, 200


@auth.login_required
def update_user():
    data = request.get_json()

    user = auth.current_user()

    try:
        if(user):
            for key, value in data.items():
                setattr(user, key, value)

            current_app.db.session.add(user)
            current_app.db.session.commit()

            return {
                "name": user.name,
                "last_name": user.last_name,
                "email": user.email
            }, 200
    except:
        return {
            "error": "missing keys or wrong keys"
        }, 400
        

@auth.login_required
def delete_user():
    user = auth.current_user()

    if(user):
        current_app.db.session.delete(user)
        current_app.db.session.commit()

        return {
            "msg": f"User {user.name} has been deleted"
        }, 200