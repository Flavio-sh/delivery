from connect import create_connection
from create_table import User


def delete_user(id):
    session = create_connection()

    user = session.get(User, id)
    session.delete(user)
    session.commit()
