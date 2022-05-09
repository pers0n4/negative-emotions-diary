from tortoise import fields, models


class User(models.Model):
    id = fields.UUIDField(pk=True)
    username = fields.CharField(max_length=255, unique=True)
    password = fields.CharField(max_length=128)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    @classmethod
    async def get_by_username(cls, username: str):
        query = cls.get_or_none(username=username)
        user = await query
        return user
