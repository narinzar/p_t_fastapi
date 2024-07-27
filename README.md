# FastAPI Todo Application

This is a simple FastAPI application for managing a list of todo items. It allows you to create, list, and retrieve items by ID.

## Features

- Create a new todo item
- List all todo items with an optional limit
- Retrieve a specific todo item by ID

## Requirements

- Python 3.7+
- FastAPI
- Pydantic

## Setup

Follow these steps to set up the project on your local machine.

### 1. Clone the Repository

```sh
git clone https://github.com/your-username/fastapi-todo-app.git
cd fastapi-todo-app
```
2. Create and Activate a Virtual Environment
It's recommended to use a virtual environment to manage dependencies. Here are the steps to create and activate a virtual environment:

#### On Windows

python -m venv venv
.\venv\Scripts\activate

#### On macOS and Linux

python3 -m venv venv
source venv/bin/activate

3. Install Dependencies
Install the required Python packages using pip:
pip install -r requirements.txt

4. Freeze Dependencies
To ensure that the exact versions of the installed packages are recorded, use pip freeze:
pip freeze > requirements.txt

5. Run the Application
Start the FastAPI server:
uvicorn main:app --reload
The application will be available at http://127.0.0.1:8000.

API Endpoints

- GET /: Returns a welcome message.
- POST /items: Creates a new todo item. Requires a JSON body with text and is_done.
- GET /items: Lists all todo items. Optional query parameter limit to limit the number of items returned.
- GET /items/{item_id}: Retrieves a specific item by its ID.

Example Usage

Create a New Item

curl -X 'POST' \
  'http://127.0.0.1:8000/items' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "Learn FastAPI",
  "is_done": false
}'

List Items

curl -X 'GET' 'http://127.0.0.1:8000/items?limit=5' -H 'accept: application/json'
Get Item by ID

curl -X 'GET' 'http://127.0.0.1:8000/items/0' -H 'accept: application/json'