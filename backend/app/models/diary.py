from typing import TYPE_CHECKING

from app.schemas.diary import Affect, Sentiment
from tortoise import fields, models

if TYPE_CHECKING:
    from .user import User


class Diary(models.Model):
    id = fields.UUIDField(pk=True)
    content = fields.TextField()
    affect = fields.CharEnumField(Affect)
    sentiment = fields.CharEnumField(Sentiment, null=True)
    sentiment_score = fields.JSONField(null=True)
    entities = fields.JSONField(default=list)
    key_phrases = fields.JSONField(default=list)
    user: fields.ForeignKeyRelation["User"] = fields.ForeignKeyField(
        "models.User", related_name="diaries"
    )
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
