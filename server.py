from flask import Flask
import os
import datetime

app = Flask(__name__)

from index import *
from endpoints.customer import *
from endpoints.product import *
from endpoints.address import *
from endpoints.errors import *
from endpoints.order import *
from endpoints.firm import *
from endpoints.auth import *
from endpoints.user import *


app.register_blueprint(user)
app.register_blueprint(auth)
app.register_blueprint(addresses)
app.register_blueprint(firm)
app.register_blueprint(customer)
app.register_blueprint(product)
app.register_blueprint(order)

#app.secret_key = "1234"

if __name__ == "__main__":
    # port = app.config.get("PORT", 5000)
    app.run(debug=True)
