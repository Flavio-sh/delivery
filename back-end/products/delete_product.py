from connect import create_connection
from create_table import Product


def delete_product(id):
    session = create_connection()

    product = session.get(Product, id)
    session.delete(product)
    session.commit()
