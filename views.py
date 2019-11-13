from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home_page():
    return render_template('home.html')

@app.route("/login")
def login_page():
    return render_template('auth/login.html')

@app.route("/about")
def about_page():
    return render_template('about.html')

@app.route("/signUp")
def signUp_page():
    return render_template('auth/signUp.html')

@app.route("/firmSignUp")
def firmSignUp_page():
    return render_template('auth/firmSignUp.html')
@app.route("/shoppingCart")
def shoppingCart_page():
    return render_template('shoppingCart.html')

