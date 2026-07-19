from sqlalchemy.orm import Session

from app.models.expense import Expense
from app.schemas.expense import ExpenseCreate, ExpenseUpdate


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

def update_expense(
    db: Session,
    expense_id: int,
    expense: ExpenseUpdate,
    user_id: int
):
    db_expense = db.query(Expense).filter(
        Expense.id == expense_id,
        Expense.user_id == user_id
    ).first()

    if not db_expense:
        return None

    db_expense.title = expense.title
    db_expense.amount = expense.amount
    db_expense.category = expense.category

    db.commit()
    db.refresh(db_expense)

    return db_expense

def delete_expense(
    db: Session,
    expense_id: int,
    user_id: int
):
    db_expense = db.query(Expense).filter(
        Expense.id == expense_id,
        Expense.user_id == user_id
    ).first()

    if not db_expense:
        return None

    db.delete(db_expense)
    db.commit()

    return {"message": "Expense deleted successfully"}