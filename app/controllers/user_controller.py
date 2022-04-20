from flask import request, jsonify, current_app
from app.models.user_model import UserModel
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from sqlalchemy.exc import IntegrityError


@jwt_required()
def get_users():
    try:
        user = get_jwt_identity()

        mapped = UserModel.query.get(user["id"])

        serialized = {
            "name": mapped.name,
            "last_name": mapped.last_name,
            "email": mapped.email
        }

        return jsonify(serialized), 200

    except:
        return {
            "error": "User not found"
        }, 404


def create_account():
    data = request.get_json()

    try:
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
            "error": "Email or Password doesn't match"
        }, 404

    serialized = {
        "id": user.id,
        "name": user.name,
        "email": user.email
    }

    access_token = create_access_token(serialized)
    
    return {
        "access_token": access_token
    }, 200


@jwt_required()
def update_user():
    data = request.get_json()

    user = get_jwt_identity()

    mapped = UserModel.query.get(user["id"])

    try:
        if(user):
            for key, value in data.items():
                setattr(mapped, key, value)

            current_app.db.session.add(mapped)
            current_app.db.session.commit()

            return {
                "name": mapped.name,
                "last_name": mapped.last_name,
                "email": mapped.email
            }, 200
    except:
        return {
            "error": "User not found"
        }, 400
        

@jwt_required()
def delete_user():
    user = get_jwt_identity()

    mapped = UserModel.query.get(user["id"])

    if(mapped):
        current_app.db.session.delete(mapped)
        current_app.db.session.commit()

        return {
            "msg": f"User {mapped.name} has been deleted"
        }, 200

    return {
        "error": "User not found"
    }, 404