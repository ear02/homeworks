from flask import Blueprint, render_template, request
from models import User, Post, db
from sqlalchemy.exc import DatabaseError
from sqlalchemy.orm import joinedload
from werkzeug.exceptions import BadRequest

posts_app = Blueprint("posts_app", __name__)


@posts_app.route("/", methods=["GET", "POST"], endpoint="posts")
def list_posts():
    if request.method == "POST":
        title = request.form.get("title")
        body = request.form.get("body")
        user = request.form.get("user")
        post = Post(title=title, body=body, user_id=user)
        db.session.add(post)
        try:
            db.session.commit()
        except DatabaseError:
            db.session.roolback()
            raise BadRequest("Incorrect data")

    posts = Post.query.options(joinedload(Post.user)).order_by(Post.id)
    users = User.query.order_by(User.id).all()
    return render_template(
        "post_list.html",
        users=users,
        posts=posts,
    )

