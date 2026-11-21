from fastapi import FastAPI
from models import User
app = FastAPI()

@app.get("/")
def root():
    return{"message": "Hola"}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}

@app.get("/search")
def search(q:str, limit:int=10):
    return {"q": q, "limit": limit}

@app.post("/users")
def create_user(user: User):
    return user