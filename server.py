from flask import Flask
import views



app = Flask(__name__)

def create_app():
    app = Flask(__name__)
    app.config.from_object("settings")

    app.add_url_rule("/", view_func=views.home_page)
    app.add_url_rule("/home", view_func=views.home_page)
    app.add_url_rule("/about", view_func=views.about_page)
    app.add_url_rule("/shoppingCart", view_func=views.shoppingCart_page)
    app.add_url_rule("/login", view_func=views.login_page)
    app.add_url_rule("/signUp", view_func=views.signUp_page)
    app.add_url_rule("/firmSignUp", view_func=views.firmSignUp_page)


    return app

if __name__ == "__main__":
    app = create_app()
    port = app.config.get("PORT", 5000)
    app.run(host="0.0.0.0", port=port)