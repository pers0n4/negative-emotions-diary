from enum import Enum
from uuid import UUID

from pydantic import BaseModel


class Affect(str, Enum):
    Hostile = "적대감"
    Irritable = "짜증"
    Ashamed = "부끄럼"
    Guilty = "죄책감"
    Distressed = "괴로움"
    Upset = "화"
    Scared = "겁"
    Afraid = "두려움"
    Jittery = "조바심"
    Nervous = "불안"


class DiaryCreate(BaseModel):
    title: str
    content: str
    affect: Affect


class DiaryRead(BaseModel):
    id: UUID
    title: str
    content: str
    affect: Affect


class Diary(BaseModel):
    id: UUID
    title: str
    content: str
    affect: Affect

    user_id: UUID

    class Config:
        orm_mode = True
