from typing import Union

from fastapi import FastAPI
from model.schema import Item
import uvicorn
import os

app = FastAPI()



@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))  # Default to 8000 locally, use Render’s PORT in production
    uvicorn.run(app, host="0.0.0.0", port=port)