from connect import create_connection
from sqlalchemy.orm import Session
from create_table import Product
from sqlalchemy import select

# Data Transfer Object


def select_product(id):
    session = create_connection()

    product = select(Product).where(Product.id.in_([f"{id}"]))

    for response in session.scalars(product):
        return response


def select_product_all():
    session = create_connection()

    product = select(Product).where(Product.id)

    json = []
    for response in session.scalars(product):
        json.append(response)

    return json
