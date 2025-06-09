from pydantic import BaseModel


class UserAdd(BaseModel):
    email: str
    password: str


class User(UserAdd):
    id: int
