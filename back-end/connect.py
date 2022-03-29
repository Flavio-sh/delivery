from sqlalchemy import create_engine
from sqlalchemy.orm import Session


def create_connection():
    engine = create_engine('mysql://root:12341234@localhost:3306/delivery', echo=True)
    session = Session(engine)
    return session
