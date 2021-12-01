from flask import Blueprint, render_template

about_app = Blueprint("about", __name__)


@about_app.route("/about/", endpoint="about")
def about_info():
    return render_template(
        "about.html"
    )