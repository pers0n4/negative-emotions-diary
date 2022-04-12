from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .initializer import init_database, init_router

app = FastAPI(
    title="Negative Emotions Diary API",
)

app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")

init_router(app)
init_database(app)
