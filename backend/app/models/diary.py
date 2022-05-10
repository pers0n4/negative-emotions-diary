
from typing import TYPE_CHECKING

from app.schemas.diary import Affect
from tortoise import fields, models

if TYPE_CHECKING:
    from .user import User


class Diary(models.Model):
    id = fields.UUIDField(pk=True)
    title = fields.CharField(max_length=100)
    content = fields.TextField()
    affect = fields.CharEnumField(Affect)
    user: fields.ForeignKeyRelation["User"] = fields.ForeignKeyField(
        "models.User", related_name="diaries"
    )
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
