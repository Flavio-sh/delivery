from connect import *
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer


engine = create_engine('mysql://root:12341234@localhost:3306/delivery', echo=True)
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    surname = Column(String(50))
    address = Column(String(50))

    def __repr__(self):
        return f"Name: {self.name}, Surname: {self.surname}, Address: {self.address}"


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    description = Column(String(50))
    price = Column(String(50))

    def __repr__(self):
        return f"Name: {self.name}, Description: {self.description}, Price: {self.price}"
