from connect import create_connection

from create_table import User


def insert_user(name, surname, address):
    session = create_connection()

    user = User(
        name=f"{name}",
        surname=f"{surname}",
        address=f"{address}"
    )

    session.add(user)
    session.commit()
