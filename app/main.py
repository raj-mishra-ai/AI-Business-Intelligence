from fastapi import FastAPI
from app.core.config import settings
from app.database.database import engine

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION
)

print("✅ Database Connected Successfully!")

@app.get("/")
def home():
    return {
        "message": "Welcome to AI Business Intelligence Platform",
        "project": settings.PROJECT_NAME,
        "version": settings.PROJECT_VERSION
    }