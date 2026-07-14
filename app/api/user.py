from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import SessionLocal
from app.schemas.user import UserCreate
from app.services.user_service import create_user

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/users")
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)