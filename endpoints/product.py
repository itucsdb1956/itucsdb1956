from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
from flask import Blueprint
import datetime
from endpoints.utils import login_required, view, login_required_action

from model.product import *

product = Blueprint('product', __name__, url_prefix='/product')

@product.route("/",methods = ["GET"])
@view
def getAllProductEnd(*args, **kwargs):
    product =  getAllProduct()
    if product is None:
        product = []
    return render_template("product/products.html", products=product,**kwargs)


@product.route("/<id>", methods=["GET"])
@view
def getProductByIdEnd(id,*args,**kwargs):
    product = getProductListById(id)
    if product is None:
        return redirect(url_for("user.feed"))
    else:
        return render_template("product/products.html", products=product[0],**kwargs)

@product.route("/create",methods = ["GET","POST"])
@login_required
@view
def createProductEnd(*args,**kwargs):

    if request.method == "GET":
        return render_template("product/createProduct.html", **kwargs)

    product_name  = request.form["product_name"]
    supplier_id  = request.form["supplier_id"]
    product_price = request.form["product_price"]


    createProduct(product_name,supplier_id,product_price)
    return redirect(url_for("product.getAllProductEnd"))

@product.route("/delete/<id>",methods =["GET","POST"])
@login_required
@view
def deleteProductByIdEnd(id, *args,**kwargs):
    deleteProduct(id)
    return (url_for("product.getAllProductEnd"))

@product.route("/update/<id>",methods = ["GET","POST"])
@login_required
@view
def updateProductByIdEnd(id,*args,**kwargs):
    product = getProductListById(id)
    if request.method == "GET":
        if product is None:
            redirect(url_for("user.feed"))
        else:
            return render_template("product/updateProduct.html", products=product[0], **kwargs)


    product_name  = request.form["product_name"]
    supplier_id  = request.form["supplier_id"]
    product_price = request.form["product_price"]

    updateProduct(id,product_name,supplier_id,product_price)

    return redirect(url_for('product.getAllProductEnd', id = id))

