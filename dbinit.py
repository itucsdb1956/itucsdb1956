import os
import sys

import psycopg2 as dbapi2


INIT_STATEMENTS = [
    """ CREATE TABLE IF NOT EXISTS ADDRESSES(
            address_id serial PRIMARY KEY,
            street_name varchar(50) NOT NULL,
            building_no integer NOT NULL,
            apartment_no integer NOT NULL,
            locality_name varchar(50) NOT NULL,
            city varchar(30) NOT NULL,
            postcode integer
            );""",

    " INSERT INTO ADDRESSES (street_name,building_no,apartment_no,locality_name,city,postcode) VALUES ('CIHAD',26,19,'KAGITHANE','ISTANBUL',34418);",
    " INSERT INTO ADDRESSES (street_name,building_no,apartment_no,locality_name,city,postcode) VALUES ('ALTINBASAK',14,9,'KAGITHANE','ISTANBUL',34418);",


    """ CREATE TABLE IF NOT EXISTS CUSTOMERS(
            customer_id serial PRIMARY KEY,
            customer_fullname varchar(50) NOT NULL,
            customer_address_id integer NOT NULL,
            customer_password varchar(40) NOT NULL,
            customer_email_address varchar(50) NOT NULL,
            customer_phone_number integer NOT NULL,
            FOREIGN KEY (customer_address_id) REFERENCES ADDRESSES(address_id) ON UPDATE CASCADE
            );""",

    " INSERT INTO CUSTOMERS (customer_fullname,customer_address_id,customer_password,customer_email_address,customer_phone_number) VALUES ('bahadir',1,'123','bahadir@gmail.com',5546674356);",

    """ CREATE TABLE IF NOT EXISTS FIRMS(
            firm_id serial PRIMARY KEY,
            firm_name varchar(50) NOT NULL,
            firm_address_id integer NOT NULL,
            firm_password varchar(40) NOT NULL,
            firm_email_address varchar(50) NOT NULL,
            firm_phone_number integer NOT NULL,
            FOREIGN KEY (firm_address_id) REFERENCES ADDRESSES(address_id) ON UPDATE CASCADE          
            );""",
    " INSERT INTO FIRMS (firm_name,firm_address_id,firm_password,firm_email_address,firm_phone_number) VALUES ('westlec',1,'123','westlec@gmail.com',2128742354);",

    """ CREATE TABLE IF NOT EXISTS PRODUCTS(
            product_id serial PRIMARY KEY,
            product_name varchar(50) NOT NULL,
            supplier_id integer NOT NULL,
            product_price decimal NOT NULL,
            FOREIGN KEY (supplier_id) REFERENCES FIRMS(firm_id) ON UPDATE CASCADE
            );""",

    " INSERT INTO PRODUCTS (product_name,supplier_id,product_price) VALUES ('kofte',1,15.75);",

    """ CREATE TABLE IF NOT EXISTS ORDERS(
            order_id serial PRIMARY KEY,
            customer_order_id integer NOT NULL,
            FOREIGN KEY (customer_order_id) REFERENCES CUSTOMERS(customer_id) ON UPDATE CASCADE
            );""",

    " INSERT INTO ORDERS (customer_order_id,) VALUES (1);",

    """ CREATE TABLE IF NOT EXISTS REGISTER_ORDER_PRODUCTS(
            register_id serial PRIMARY KEY,
            register_order_id integer NOT NULL,
            register_product_id integer NOT NULL,
            FOREIGN KEY (register_order_id) REFERENCES ORDERS(order_id) ON UPDATE CASCADE
            FOREIGN KEY (register_product_id) REFERENCES PRODUCTS(product_id) ON UPDATE CASCADE
            );""",

    " INSERT INTO PRODUCTS (register_order_id,register_product_id) VALUES (1,1);",

]


def initialize(url):
    with dbapi2.connect(url) as connection:
        cursor = connection.cursor()
        for statement in INIT_STATEMENTS:
            cursor.execute(statement)
        cursor.close()


if __name__ == "__main__":
    url = os.getenv("DATABASE_URL")
    if url is None:
        print("Usage: DATABASE_URL=url python dbinit.py", file=sys.stderr)
        sys.exit(1)
    initialize(url)
