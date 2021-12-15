import os

from flask import Flask, render_template
from views import users_app, posts_app

from models import db
app = Flask(__name__)
app.register_blueprint(users_app, url_prefix="/users")
app.register_blueprint(posts_app, url_prefix="/posts")

CONFIG_OBJ_PATH = "config.{}".format(os.getenv("CONFIG", "DevelopmentConfig"))
app.config.from_object(CONFIG_OBJ_PATH)

db.init_app(app)

with app.app_context():
    db.drop_all()
    db.create_all()


@app.route("/", endpoint="startpage")
def root():
    return render_template(
        "base.html"
    )


if __name__ == '__main__':
    app.run(host="0.0.0.0")
