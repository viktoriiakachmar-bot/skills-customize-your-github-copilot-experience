# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API using FastAPI to practice route creation, request handling, JSON responses, and basic CRUD operations.

## 📝 Tasks

### 🛠️ Create the FastAPI App

#### Description
Set up a simple FastAPI application and define a health check endpoint that confirms the API is running.

#### Requirements
Completed program should:

- Import `FastAPI` and create an app instance.
- Define a route that responds to `GET /health`.
- Return a JSON response such as:
  ```json
  {"status": "ok"}
  ```
- Ensure the app can be launched with `uvicorn`.

### 🛠️ Build CRUD Endpoints

#### Description
Create endpoints to manage a list of tasks or items using RESTful conventions.

#### Requirements
Completed program should:

- Use an in-memory list to store items.
- Add a `GET /items` endpoint that returns all items.
- Add a `POST /items` endpoint that accepts JSON data and creates a new item.
- Add a `GET /items/{item_id}` endpoint that returns one item by ID.
- Add a `PUT /items/{item_id}` or `DELETE /items/{item_id}` endpoint to update or remove an item.
- Return a clear error response when a requested item does not exist.
- Example request:
  ```json
  {
    "name": "Finish homework",
    "done": false
  }
  ```
- Example response:
  ```json
  {
    "id": 1,
    "name": "Finish homework",
    "done": false
  }
  ```
