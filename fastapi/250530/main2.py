from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI()

items = []


class Item(BaseModel):
    name: str
    price: float = 0.0


@app.get("/item")
def item_list():
    return {"item": items}


@app.post("/item/create")
def create_item(item: Item):
    items.append(item)
    print(item.name, item.price)
    return {"item": item}


@app.put("/item/{item_id}")
def item_update(item_id: int, item: Item):
    items[item_id - 1] = item
    return {"item": item}


users = []


class User(BaseModel):
    name: str
    email: str
    age: int


@app.post("/users")
def user_create(user: User):
    users.append(user)
    return {"등록된 유저": user}


@app.get("/users")
def user_list():
    return {"유저리스트": users}


@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    del users[user_id - 1]
