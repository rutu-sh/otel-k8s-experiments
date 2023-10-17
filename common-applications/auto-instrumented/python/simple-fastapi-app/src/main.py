import os
import logging

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from starlette.responses import JSONResponse

os.environ["LOG_LEVEL"] = "DEBUG"
logger = logging.getLogger(__name__)
logger.setLevel(level=logging.DEBUG)


class Item(BaseModel):
    name: str
    price: float
items = []

app = FastAPI()


@app.get("/")
def health_check():
    logger.info("Health check called")
    return JSONResponse(status_code=200, content={"message": "Application is up and running"})


@app.get("/rest/v1/items")
def get_items():
    logger.info("Get items called")
    return JSONResponse(status_code=200, content={"items": {item_id: item.dict() for item_id, item in enumerate(list(filter(None, items)))}})


@app.get("/rest/v1/item/{id}", response_model=Item)
def get_item(id: int):
    logger.info("Get items called")
    try:
        if items[id] is None:
            logger.error(f"Item not found for id: {id}")
            return JSONResponse(status_code=404, content={"message": "Item not found"})
        logger.debug(f"Item found for id: {id}")
        return items[id]
    except IndexError:
        logger.error(f"Item not found for id: {id}")
        return JSONResponse(status_code=404, content={"message": "Item not found"})


@app.post("/rest/v1/item")
def add_item(item: Item):
    logger.info("Add item called")
    items.append(item)
    return JSONResponse(status_code=201, content={"message": "Item added successfully", "item_id": len(items) - 1})


@app.delete("/rest/v1/item/{id}")
def delete_item(id: int):
    logger.info("Delete item called")
    try:
        logger.debug(f"Deleting item for id: {id}")
        items[id] = None
        logger.debug(f"Item deleted for id: {id}")
        return JSONResponse(status_code=200, content={"message": "Item deleted successfully"})
    except IndexError:
        logger.error(f"Item not found for id: {id}")
        return JSONResponse(status_code=404, content={"message": "Item not found"})


@app.put("/rest/v1/item/{id}")
def update_item(id: int, item: Item):
    logger.info("Update item called")
    try:
        logger.debug(f"Updating item for id: {id}")
        items[id] = item
        logger.debug(f"Item updated for id: {id}")
        return JSONResponse(status_code=200, content={"message": "Item updated successfully"})
    except IndexError:
        return JSONResponse(status_code=404, content={"message": "Item not found"})


def main():
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
