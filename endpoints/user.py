"""
This module is for user endpoints
It has CRUD endpoints
"""

from flask import Flask, flash, redirect, render_template, request, session, abort
from flask import Blueprint

from endpoints.utils import login_required, view

user = Blueprint('user', __name__, url_prefix='/user')


@user.route("/feed", methods=["GET"])
@login_required
@view
def feed(*args, **kwargs):
    """
    Welcome page user
    """
    return render_template("user/feed.html", **kwargs)


@user.route("/profile", methods=["GET"])
@login_required
@view
def profile(*args, **kwargs):
    """
    It renders profile page which contains some redirections for operations
    """
    return render_template("user/profile.html", **kwargs)

