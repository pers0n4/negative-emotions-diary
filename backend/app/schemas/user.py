from uuid import UUID

from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserRead(BaseModel):
    id: UUID
    email: EmailStr


class User(BaseModel):
    id: UUID
    email: EmailStr
    password: str

    class Config:
        orm_mode = True
