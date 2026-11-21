from pydantic import BaseModels

class User(BaseModel):
    name: str
    age: int