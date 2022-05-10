from uuid import UUID

from pydantic import BaseModel


class DiaryCreate(BaseModel):
    title: str
    content: str


class DiaryRead(BaseModel):
    id: UUID
    title: str
    content: str


class Diary(BaseModel):
    id: UUID
    title: str
    content: str

    user_id: UUID

    class Config:
        orm_mode = True
