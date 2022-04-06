from fastapi import FastAPI

from .initializer import init_database

app = FastAPI(
    title="Negative Emotions Diary API",
)

init_database(app)
