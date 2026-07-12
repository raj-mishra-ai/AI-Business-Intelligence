from fastapi import FastAPI

from app.core.config import settings
from app.database.database import Base, engine
from app.models.company import Company
from app.api.company import router as company_router

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION
)

Base.metadata.create_all(bind=engine)

app.include_router(company_router)

print("✅ Database Connected Successfully!")


@app.get("/")
def home():
    return {
        "message": "Welcome to AI Business Intelligence Platform",
        "project": settings.PROJECT_NAME,
        "version": settings.PROJECT_VERSION
    }