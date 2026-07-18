from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import SessionLocal
from app.dependencies.auth import verify_token
from app.schemas.expense import ExpenseCreate
from app.services.expense_service import (
    create_expense,
    get_expenses
)

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/expenses")
def add_expense(
    expense: ExpenseCreate,
    db: Session = Depends(get_db),
    current_user=Depends(verify_token)
):
    return create_expense(
        db,
        expense,
        current_user.id
    )


@router.get("/expenses")
def read_expenses(
    db: Session = Depends(get_db),
    current_user=Depends(verify_token)
):
    return get_expenses(
        db,
        current_user.id
    )