from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()

items = {}


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    active: bool = True


class ItemUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None


@app.post("/items/{item_id}", response_model=Item)
def create_item(item_id: int, item: Item):
    if item_id in items:
        raise HTTPException(status_code=400, detail="Item already exists")
    items[item_id] = item

    return item


@app.get("/items", response_model=List[Item])
def read_items():
    return list(items.values())


@app.get("/items-keys", response_model=List[int])
def read_keys():
    return list(items.keys())


@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]


@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: ItemUpdate):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")

    stored_item: Item = items[item_id]
    print(
        f"stored_item name={stored_item.name} price={stored_item.price} description={stored_item.description}"
    )
    update_data = item.model_dump(exclude_unset=True)

    print(update_data)

    updated_item = stored_item.model_copy(update=update_data)

    print(
        f"update_item name={updated_item.name} price={updated_item.price} description= {updated_item.description}"
    )

    items[item_id] = updated_item
    return updated_item


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")

    items.pop(item_id)

@app.put("/items/{item_id}/active")
def update_active(item_id:int,status:bool):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    stored_item: Item = items[item_id]
    
    if stored_item.active == status:
        raise HTTPException(status_code=400,detail="이미 활성화되었거나 비활성화된 아이템입니다.")
    
    stored_item.active = status

    return stored_item
