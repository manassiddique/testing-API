from fastapi import FastAPI
from typing import List, Dict

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

# Fake users data
fake_users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
    {"id": 3, "name": "Charlie", "email": "charlie@example.com"}
]

# Fake posts data
fake_posts = [
    {"id": 1, "title": "First Post", "content": "This is the first post.", "user_id": 1},
    {"id": 2, "title": "Second Post", "content": "This is the second post.", "user_id": 2},
    {"id": 3, "title": "Third Post", "content": "This is the third post.", "user_id": 1}
]

@app.get("/users")
def get_users() -> List[Dict]:
    return fake_users

@app.get("/users/{user_id}")
def get_user(user_id: int) -> Dict:
    user = next((u for u in fake_users if u["id"] == user_id), None)
    if not user:
        return {"error": "User not found"}
    return user

@app.get("/posts")
def get_posts() -> List[Dict]:
    return fake_posts

@app.get("/posts/{post_id}")
def get_post(post_id: int) -> Dict:
    post = next((p for p in fake_posts if p["id"] == post_id), None)
    if not post:
        return {"error": "Post not found"}
    return post
