from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import SessionLocal
from app.dependencies.auth import verify_token
from app.schemas.expense import ExpenseCreate, ExpenseUpdate
from app.services.expense_service import (
    create_expense,
    get_expenses,
    update_expense,
    delete_expense,
    get_dashboard_summary,
    get_category_summary
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


@router.put("/expenses/{expense_id}")
def edit_expense(
    expense_id: int,
    expense: ExpenseUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(verify_token)
):
    updated_expense = update_expense(
        db,
        expense_id,
        expense,
        current_user.id
    )

    if not updated_expense:
        return {"message": "Expense not found"}

    return updated_expense


@router.delete("/expenses/{expense_id}")
def remove_expense(
    expense_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(verify_token)
):
    deleted_expense = delete_expense(
        db,
        expense_id,
        current_user.id
    )

    if not deleted_expense:
        return {"message": "Expense not found"}

    return deleted_expense


@router.get("/dashboard/summary")
def dashboard_summary(
    db: Session = Depends(get_db),
    current_user=Depends(verify_token)
):
    return get_dashboard_summary(
        db,
        current_user.id
    )


@router.get("/dashboard/category-summary")
def category_summary(
    db: Session = Depends(get_db),
    current_user=Depends(verify_token)
):
    return get_category_summary(
        db,
        current_user.id
    )