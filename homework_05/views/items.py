from flask import Blueprint, render_template, request, redirect, url_for

items_app = Blueprint("items", __name__)

ITEMS = {}


@items_app.route("/add/", methods=["GET", "POST"], endpoint="add")
def add_item():
    if request.method == "GET":
        return render_template(
            "add_items.html"
        )

    item_name = request.form.get("item_name")
    item_id = len(ITEMS) + 1
    ITEMS[item_id] = item_name

    return redirect(url_for("startpage"))
