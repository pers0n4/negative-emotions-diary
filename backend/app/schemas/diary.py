from datetime import datetime
from enum import Enum
from typing import Optional
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


class Sentiment(Enum):
    POSITIVE = "POSITIVE"  # 긍정
    NEGATIVE = "NEGATIVE"  # 부정
    NEUTRAL = "NEUTRAL"  # 중립
    MIXED = "MIXED"  # 혼합


class Entity(BaseModel):
    Score: str
    Type: str
    Text: str
    BeginOffset: int
    EndOffset: int


class KeyPhrase(BaseModel):
    Score: float
    Text: str
    BeginOffset: int
    EndOffset: int


class DiaryCreate(BaseModel):
    content: str
    affect: Affect


class DiaryRead(BaseModel):
    id: UUID
    content: str
    affect: Affect
    sentiment: Optional[Sentiment] = None
    sentiment_score: Optional[dict[str, float]] = None
    entities: Optional[list[Entity]] = []
    key_phrases: Optional[list[KeyPhrase]] = []
    created_at: datetime
    updated_at: datetime


class Diary(BaseModel):
    id: UUID
    content: str
    affect: Affect
    sentiment: Optional[Sentiment] = None
    sentiment_score: Optional[dict[str, float]] = None
    entities: Optional[list[Entity]] = []
    key_phrases: Optional[list[KeyPhrase]] = []
    user_id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
