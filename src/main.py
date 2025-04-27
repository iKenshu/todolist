from contextlib import asynccontextmanager

from fastapi import FastAPI
from mangum import Mangum

from config.database import init_db
from router import api_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(
    title="Todo API",
    description="API for Todo app",
    version="1.0.0",
    lifespan=lifespan,
)

app.include_router(api_router, prefix="/api")


@app.get("/")
def root():
    return {"message": "Go to /docs"}


handler = Mangum(app)
