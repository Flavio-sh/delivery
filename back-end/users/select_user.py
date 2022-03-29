from connect import create_connection
from create_table import User
from sqlalchemy import select

# Data Transfer Object


def select_user(id):
    session = create_connection()
    product = select(User).where(User.id.in_([f"{id}"]))

    for response in session.scalars(product):
        return response


def select_user_all():
    session = create_connection()
    product = select(User).where(User.id)

    json = []
    for response in session.scalars(product):
        json.append(response)

    return json
