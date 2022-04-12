from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .initializer import init_database, init_router

app = FastAPI(
    title="Negative Emotions Diary API",
)

app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")


@app.get("/", response_class=RedirectResponse)
async def index_page():
    return "/signin"


@app.get("/signin", response_class=HTMLResponse)
async def signin_page(request: Request):
    return templates.TemplateResponse("signin.html", {"request": request})


@app.get("/signup", response_class=HTMLResponse)
async def signup_page(request: Request):
    return templates.TemplateResponse("signup.html", {"request": request})


init_router(app)
init_database(app)
