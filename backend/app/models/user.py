from typing import TYPE_CHECKING

from tortoise import fields, models

if TYPE_CHECKING:
    from .diary import Diary


class User(models.Model):
    id = fields.UUIDField(pk=True)
    email = fields.CharField(max_length=255, unique=True)
    password = fields.CharField(max_length=128)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    diaries: fields.ReverseRelation["Diary"]

    @classmethod
    async def get_by_email(cls, email: str):
        query = cls.get_or_none(email=email)
        user = await query
        return user
