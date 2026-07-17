from fastapi import FastAPI, Request

from app.core.config import settings
from app.database.database import Base, engine
from app.models.company import Company
from app.models.user import User
from app.api.company import router as company_router
from app.api.user import router as user_router

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION
)

Base.metadata.create_all(bind=engine)

app.include_router(company_router)
app.include_router(user_router)


@app.middleware("http")
async def debug_errors(request: Request, call_next):
    try:
        response = await call_next(request)
        return response
    except Exception:
        import traceback
        traceback.print_exc()
        raise


print("Database Connected Successfully!")