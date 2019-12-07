from flask import Blueprint
from flask import Flask, flash, redirect, render_template, request, session, abort, url_for

from endpoints.utils import *
from model.user import get_user, create_user,getUserId
from model.address import createAddress, getAddressId
from model.customer import createCustomer

auth = Blueprint('auth', __name__, url_prefix='/auth')

@auth.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "GET":
        if "logged_in" in session:
            return redirect(url_for("user.feed"))
        return render_template("auth/login.html")



    print("login")
    user = get_user(request.form["email"], request.form["password"])
    print(request.form["email"], request.form["password"])
    if user is not None:
        session["logged_in"] = user
        return redirect(user.feed)
    else:
        return render_template("auth/login.html", msg="Wrong password or email address try again!")



@auth.route("/logout",methods= ["GET"])
@login_required
def logout():
    if session:
        session.clear()
    return redirect((url_for("home")))


@auth.route("/signUp", methods=["GET", "POST"])
@view
def signUp(*args, **kwargs):

    if "logged_in" in session:
        return redirect(url_for("user.feed"))
    if request.method == "GET":
        return render_template("auth/signUp.html", **kwargs)

    username = request.form["username"]
    password = request.form["password"]
    usertype = 0
    email    = request.form["email"]

    fullname  = request.form["Full_Name"]
    phone     = request.form["Mobile_Number"]
    locality  = request.form["Locality"]
    street    = request.form["Street"]
    building  = request.form["Building"]
    apartment = request.form["Apartment"]
    city      = request.form["City"]
    postcode  = request.form["Pin_Code"]
    credit    = request.form["Credit_Card"]
    country   = request.form["Country"]


    NewAddress  = createAddress(street,building,apartment,locality,city,postcode)
    print(NewAddress)
    adressid    =  getAddressId(street,building,apartment,locality,city,postcode)

    NewUser     = create_user(username, password, email, usertype)
    print(NewUser)
    userid = getUserId(username, password, email, usertype)

    NewCustomer = createCustomer(fullname, adressid, phone, userid)
    print(NewCustomer)

    if NewUser is None:
        return render_template("auth/signUp.html", msg="Record process is not done.", **kwargs)
    return redirect(url_for("feed"))


@auth.route("/firmSignUp", methods=["GET", "POST"])
@view
def firmsignUp(*args, **kwargs):

    if "logged_in" in session:
        return redirect(url_for("user.feed"))
    if request.method == "GET":
        return render_template("auth/firmSignUp.html", **kwargs)

    username = request.form["username"]
    password = request.form["password"]
    usertype = 1
    email    = request.form["email"]



    NewUser = create_user(username,password,email,usertype)

    if NewUser is None:
        return render_template("auth/firmSignUp.html", msg="Record process is not done.", **kwargs)
    return redirect(url_for("feed"))

