from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Task API")

# In-memory storage for tasks
items = [
    {"id": 1, "name": "Write README", "done": False},
    {"id": 2, "name": "Review notes", "done": True},
]


class Item(BaseModel):
    name: str
    done: bool = False


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/items")
def get_items():
    return items


@app.post("/items")
def create_item(item: Item):
    # TODO: create a new item with a unique id and append it to the list
    pass


@app.get("/items/{item_id}")
def get_item(item_id: int):
    # TODO: return the item that matches the requested id
    pass


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    # TODO: update the matching item and return the new data
    pass


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    # TODO: remove the item and return a success message
    pass
