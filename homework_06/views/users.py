from flask import Blueprint, render_template, request
from models import User, db
from sqlalchemy.exc import DatabaseError
from werkzeug.exceptions import BadRequest


users_app = Blueprint("users_app", __name__)


@users_app.route("/", methods=["GET", "POST"], endpoint="users")
def list_users():
    if request.method == "POST":
        user_name = request.form.get("username")
        name = request.form.get("name")
        email = request.form.get("email")
        user = User(username=user_name, name=name, email=email)
        db.session.add(user)
        try:
            db.session.commit()
        except DatabaseError:
            db.session.roolback()
            raise BadRequest("Incorrect data")

    users = User.query.order_by(User.id).all()
    return render_template(
        "user_list.html",
        users=users,
    )

