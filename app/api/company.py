from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import SessionLocal
from app.schemas.company import CompanyCreate, CompanyResponse
from app.services.company_service import (
    create_company,
    get_companies,
    get_company_by_id,
    update_company,
    delete_company,
)

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


@router.get("/companies", response_model=list[CompanyResponse])
def get_all_companies(db: Session = Depends(get_db)):
    return get_companies(db)


@router.get("/companies/{company_id}", response_model=CompanyResponse)
def get_company(company_id: int, db: Session = Depends(get_db)):
    company = get_company_by_id(db, company_id)

    if company is None:
        raise HTTPException(status_code=404, detail="Company not found")

    return company


@router.put("/companies/{company_id}", response_model=CompanyResponse)
def edit_company(
    company_id: int,
    company: CompanyCreate,
    db: Session = Depends(get_db),
):
    updated_company = update_company(db, company_id, company)

    if updated_company is None:
        raise HTTPException(status_code=404, detail="Company not found")

    return updated_company


@router.delete("/companies/{company_id}", response_model=CompanyResponse)
def remove_company(company_id: int, db: Session = Depends(get_db)):
    deleted_company = delete_company(db, company_id)

    if deleted_company is None:
        raise HTTPException(status_code=404, detail="Company not found")

    return deleted_company