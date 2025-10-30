# Users Mini API — FastAPI + SQLModel + SQLite

## English

### Overview
A tiny FastAPI + SQLModel + SQLAlchemy project demonstrating CRUD for a single entity `User` on SQLite.

**What it shows**
- Pydantic-style request/response schemas: `UserCreate`, `UserRead`, `UserUpdate`
- SQLModel table model: `User`
- SQLAlchemy session usage: `create_engine`, `Session`, `commit`, `refresh`
- FastAPI routes: Create / Read / List (pagination) / Patch / Delete

### Requirements
- Python 3.11+
- See `requirements.txt`

### Quick Start

# 0) (optional) create venv
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate

# 1) install
pip install -r requirements.txt

# 2) run
uvicorn main:app --reload
# -> http://127.0.0.1:8000/docs

| Method | Path               | Purpose                 | Params / Body                          | Response           |
| -----: | ------------------ | ----------------------- | -------------------------------------- | ------------------ |
|   POST | `/users`           | Create a user           | body: `{"name":"Alice"}`               | `UserRead`         |
|    GET | `/users/{user_id}` | Get a user by id        | path: `user_id:int`                    | `UserRead`         |
|    GET | `/users`           | List users (pagination) | query: `offset>=0`, `1<=limit<=100`    | `List[UserRead]`   |
|  PATCH | `/users/{user_id}` | Partially update `name` | body: `{"name":"New Name"}` (optional) | `UserRead`         |
| DELETE | `/users/{user_id}` | Delete a user           | path: `user_id:int`                    | **204 No Content** |

Quick Test (curl)
# Create
curl -sX POST http://127.0.0.1:8000/users \
  -H 'Content-Type: application/json' -d '{"name":"Alice"}'

# Get by id
curl -s http://127.0.0.1:8000/users/1

# List with pagination
curl -s 'http://127.0.0.1:8000/users?offset=0&limit=2'

# Patch name
curl -sX PATCH http://127.0.0.1:8000/users/1 \
  -H 'Content-Type: application/json' -d '{"name":"Alice Chen"}'

# Delete (expects 204)
curl -i -X DELETE http://127.0.0.1:8000/users/1

Notes

UserUpdate.name is optional; only provided fields are updated.

Ensure tables exist at startup (e.g., call SQLModel.metadata.create_all(engine)).

To reset, stop the server and delete app.db, then start again.
