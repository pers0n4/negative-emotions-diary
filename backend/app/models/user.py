from tortoise import fields, models


class User(models.Model):
    id = fields.UUIDField(pk=True)
    email = fields.CharField(max_length=255, unique=True)
    password = fields.CharField(max_length=128)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    @classmethod
    async def get_by_email(cls, email: str):
        query = cls.get_or_none(email=email)
        user = await query
        return user
