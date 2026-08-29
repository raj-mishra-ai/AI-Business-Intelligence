from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware


from app.utils.logger import logger
from app.core.config import settings
from app.database.database import Base, engine

from app.models.company import Company
from app.models.user import User
from app.models.expense import Expense

from app.api.company import router as company_router
from app.api.user import router as user_router
from app.api.expense import router as expense_router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5174",
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



logger.info("Application Started Successfully")

Base.metadata.create_all(bind=engine)

app.include_router(company_router)
app.include_router(user_router)
app.include_router(expense_router)


@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(
        f"Request: {request.method} {request.url}"
    )

    try:
        response = await call_next(request)

        logger.info(
            f"Response Status: {response.status_code}"
        )

        return response

    except Exception as e:
        logger.error(
            f"Error: {str(e)}"
        )
        raise


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