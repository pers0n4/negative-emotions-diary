from app.models import Diary, User
from fastapi import FastAPI
from tortoise import run_async
from tortoise.contrib.fastapi import register_tortoise
from yaml import load

try:
    from yaml import CDumper as Dumper
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Dumper, Loader

from app.core.auth import get_password_hash


def init_router(app: FastAPI):
    from app.routers import affect, auth, diary, user

    app.include_router(user.router)
    app.include_router(auth.router)
    app.include_router(diary.router)
    app.include_router(affect.router)


def init_database(app: FastAPI):
    register_tortoise(
        app,
        db_url="sqlite://:memory:",
        modules={"models": ["app.models"]},
        generate_schemas=True,
        add_exception_handlers=True,
    )


async def init_data():
    with open("./data/data.yaml", "r") as f:
        data = load(f, Loader=Loader)

        user = await User.create(
            email="test@example.org", password=get_password_hash("test")
        )

        await Diary.bulk_create(
            [
                Diary(content=item["content"], affect=item["affect"], user_id=user.id)
                for item in data
            ]
        )
