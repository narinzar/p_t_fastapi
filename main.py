# Importing FastAPI class to create the app and HTTPException to handle errors
from fastapi import FastAPI, HTTPException
# Importing BaseModel from pydantic to define data models
from pydantic import BaseModel

# Creating an instance of the FastAPI class
app = FastAPI()

# Defining a Pydantic model for the item with two fields: text and is_done
class Item(BaseModel):
    text: str              # The main content of the item, a string
    is_done: bool = False  # A boolean indicating if the item is done, defaults to False

# A list to store the items created by the user
items = []

# Defining a root endpoint that returns a simple "Hello World" message
@app.get("/")
def root():
    return {"message": "Hello World"}

# Endpoint to create a new item; it accepts an Item object in the request body
@app.post("/items")
def create_item(item: Item):
    items.append(item)  # Adding the new item to the items list
    return items        # Returning the updated list of items

# Endpoint to list items with an optional limit on the number of items returned
@app.get("/items", response_model=list[Item])
def list_items(limit: int = 10):
    return items[0:limit]  # Returning a slice of the items list up to the limit

# Endpoint to get a specific item by its ID
@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int) -> Item:
    # If the item_id is valid, return the corresponding item
    if item_id < len(items):
        return items[item_id]
    else:
        # Raise an HTTP 404 exception if the item_id is not found
        raise HTTPException(status_code=404, detail=f"Item {item_id} not found")
