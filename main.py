from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List
from uuid import uuid4, UUID

app = FastAPI()

class Item(BaseModel):
    id: Optional[UUID] = uuid4()
    name: str
    description: Optional[str] = None

items = []

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/", response_model=List[Item])
def read_items():
    return items

@app.post("/items/", response_model=Item)
def create_item(item: Item):
    items.append(item)
    return item

@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: UUID):
    for item in items:
        if item.id == item_id:
            return item
    return {"error": "Item not found"}
