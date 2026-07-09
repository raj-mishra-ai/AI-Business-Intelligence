from fastapi import FastAPI
from app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION
)


@app.get("/")
def home():
    return {
        "message": "Welcome to AI Business Intelligence Platform",
        "project": settings.PROJECT_NAME,
        "version": settings.PROJECT_VERSION
    }