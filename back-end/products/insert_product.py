from connect import create_connection

from create_table import Product


def insert_product(name, description, price):
    session = create_connection()

    product = Product(
        name=f"{name}",
        description=f"{description}",
        price=f"{price}"
    )

    session.add(product)
    session.commit()
