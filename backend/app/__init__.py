from fastapi import FastAPI

from .initializer import init_database, init_router

app = FastAPI(
    title="Negative Emotions Diary API",
)

init_router(app)
init_database(app)
