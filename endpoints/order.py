
from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
from flask import Blueprint

from endpoints.utils import  login_required ,view ,login_required_action

from model.order import *

order = Blueprint ('order' ,__name__, url_prefix='/order')

@order.route("/", methods=["GET"])
@view
def getAllOrderEnd(*args, **kwargs):

    orderAll = getAllOrder()
    if orderAll is None:
        orderAll = []
    return render_template("order/orders.html", orders = orderAll, **kwargs)

@order.route("/<id>", methods = ["GET"])
@view
def getOrderByIdEnd(id ,*args ,**kwargs):

    order = getOrderListById(id)
    if order is None:
        return redirect(url_for("user.feed"))
    else:
        return render_template("order/orders.html", orders = order[0],**kwargs)


@order.route("/create", methods = ["GET" ,"POST"])
@login_required
@view
def createOrderEnd(*args ,**kwargs):
    if request.method == "GET":
        return render_template(("order/createOrder.html", *kwargs))

    product_id = request.form["product_id"]
    customer_order_id =  request.form["customer_order_id"]
    createOrder(product_id , customer_order_id)
    return redirect(url_for("order.getAllOrderEnd"))


@order.route("/delete/<id>" ,methods = ["GET" ,"POST"])
@login_required
@view
def deleteOrderEnd(id ,*args ,**kwargs):
    deleteOrderById(id)
    return redirect(url_for("order.getAllOrderEnd"))


@order.route("/update/<id>", methods =["GET" ,"POST"])
@login_required
@view
def updateOrderEnd(id ,*args ,**kwargs):

    order = getOrderListById(id)
    if request.method == "GET":
        if order is None:
            redirect(url_for("user.feed"))
        else:
            return render_template("order/updateOrders.html", orders= order)

    product_id = request.form["product_id"]
    customer_order_id = request.form["customer_order_id"]


    updateOrder(id,product_id  ,customer_order_id )

    return redirect(url_for('order.getOrderByIdEnd', id = id))



