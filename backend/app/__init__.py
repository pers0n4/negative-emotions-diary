from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .initializer import init_data, init_database, init_router

app = FastAPI(
    title="Negative Emotions Diary API",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

init_router(app)
init_database(app)


@app.on_event("startup")
async def startup_event():
    await init_data()
