from uuid import UUID

from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str
    password: str


class UserRead(BaseModel):
    id: UUID
    username: str


class User(BaseModel):
    id: UUID
    username: str
    password: str

    class Config:
        orm_mode = True
