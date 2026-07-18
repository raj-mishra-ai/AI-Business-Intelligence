from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.database.database import SessionLocal
from app.schemas.user import UserCreate
from app.services.user_service import create_user, authenticate_user
from app.utils.jwt_handler import create_access_token
from app.dependencies.auth import verify_token

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


@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    print("Username:", form_data.username)
    print("Password:", form_data.password)

    db_user = authenticate_user(
        db,
        form_data.username,
        form_data.password
    )

    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    access_token = create_access_token(
        data={"sub": db_user.email}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


@router.get("/me")
def get_current_user(current_user=Depends(verify_token)):
    return {
        "id": current_user.id,
        "username": current_user.username,
        "email": current_user.email
    }