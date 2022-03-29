# uvicorn main:app --reload

from products import delete_product, select_product, insert_product, product_model
from users import delete_user, insert_user, select_user, user_model
from start_app import *

app = start_app()


@app.get("/")
async def root():
    return "Api básica para consulta"


@app.get("/products")
async def root():
    json = select_product.select_product_all()
    return json


@app.get("/products/{id}")
async def root(id):
    json = select_product.select_product(id)
    return json


@app.post("/products")
async def create_item(product: product_model.Product):

    insert_product.insert_product(
        product.name,
        product.price,
        product.description,)
    json = select_product.select_product_all()

    return json


@app.delete("/products/{id}")
async def delete_item(id):
    delete_product.delete_product(id)
    json = select_product.select_product_all()

    return json


@app.get("/users")
async def root():
    json = select_user.select_user_all()
    return json


@app.get("/users/{id}")
async def root(id):
    json = select_user.select_user(id)
    return json


@app.post("/users")
async def create_item(user: user_model.User):

    insert_user.insert_user(
        user.name,
        user.surname,
        user.address,)
    json = select_user.select_user_all()

    return json


@app.delete("/users/{id}")
async def delete_item(id):
    delete_user.delete_user(id)
    json = select_user.select_user_all()

    return json
