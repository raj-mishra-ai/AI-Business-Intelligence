from sqlalchemy.orm import Session

from app.models.expense import Expense
from app.schemas.expense import ExpenseCreate


def create_expense(db: Session, expense: ExpenseCreate, user_id: int):
    new_expense = Expense(
        title=expense.title,
        amount=expense.amount,
        category=expense.category,
        user_id=user_id
    )

    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)

    return new_expense


def get_expenses(db: Session, user_id: int):
    return db.query(Expense).filter(
        Expense.user_id == user_id
    ).all()