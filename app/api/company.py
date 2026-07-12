from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import SessionLocal
from app.schemas.company import CompanyCreate, CompanyResponse
from app.services.company_service import create_company

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/companies", response_model=CompanyResponse)
def add_company(company: CompanyCreate, db: Session = Depends(get_db)):
    return create_company(db, company)