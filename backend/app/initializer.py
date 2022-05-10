from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise


def init_router(app: FastAPI):
    from app.routers import auth, diary, user

    app.include_router(user.router)
    app.include_router(auth.router)
    app.include_router(diary.router)


def init_database(app: FastAPI):
    register_tortoise(
        app,
        db_url="sqlite://:memory:",
        modules={"models": ["app.models"]},
        generate_schemas=True,
        add_exception_handlers=True,
    )
