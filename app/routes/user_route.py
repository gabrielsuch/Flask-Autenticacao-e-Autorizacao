from flask import Blueprint
from app.controllers.user_controller import get_users, create_account, login, update_user, delete_user


bp = Blueprint("api", __name__, url_prefix="/api")


bp.get("")(get_users)
bp.post("/signup")(create_account)
bp.post("/signin")(login)
bp.put("")(update_user)
bp.delete("")(delete_user)