"""
Домашнее задание №5
Первое веб-приложение

создайте базовое приложение на Flask
создайте index views /
добавьте страницу /about/, добавьте туда текст
создайте базовый шаблон (используйте https://getbootstrap.com/docs/5.0/getting-started/introduction/#starter-template)
в базовый шаблон подключите статику Bootstrap 5 и добавьте стили, примените их
в базовый шаблон добавьте навигационную панель nav (https://getbootstrap.com/docs/5.0/components/navbar/)
в навигационную панель добавьте ссылки на главную страницу / и на страницу /about/ при помощи url_for
"""
from flask import Flask, render_template
from views.about import about_app
from views.items import items_app, ITEMS


app = Flask(__name__)
app.register_blueprint(about_app, url_prefix="/")
app.register_blueprint(items_app, url_prefix="/items")


@app.route("/", endpoint="startpage")
def root():

    print(ITEMS.items())

    return render_template(
        "base.html",
        items=ITEMS.items()
    )



if __name__ == '__main__':
    app.run(debug=True)
