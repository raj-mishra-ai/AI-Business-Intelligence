from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import SessionLocal
from app.schemas.company import CompanyCreate, CompanyUpdate
from app.services.company_service import (
    create_company,
    get_companies,
    get_company_by_id,
    update_company,
    delete_company,
    get_company_summary,
    search_company,
    filter_by_industry,
    filter_by_country,
)

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/companies")
def add_company(
    company: CompanyCreate,
    db: Session = Depends(get_db)
):
    return create_company(db, company)


@router.get("/companies")
def read_companies(
    db: Session = Depends(get_db)
):
    return get_companies(db)


@router.get("/companies/search")
def search_company_by_name(
    company_name: str,
    db: Session = Depends(get_db)
):
    return search_company(db, company_name)


@router.get("/companies/summary")
def company_summary(
    db: Session = Depends(get_db)
):
    return get_company_summary(db)


@router.get("/companies/filter/industry")
def get_companies_by_industry(
    industry: str,
    db: Session = Depends(get_db)
):
    return filter_by_industry(db, industry)

@router.get("/companies/filter/country")
def get_companies_by_country(
    country: str,
    db: Session = Depends(get_db)
):
    return filter_by_country(db, country)


@router.get("/companies/{company_id}")
def read_company(
    company_id: int,
    db: Session = Depends(get_db)
):
    company = get_company_by_id(db, company_id)

    if not company:
        return {"message": "Company not found"}

    return company


@router.put("/companies/{company_id}")
def edit_company(
    company_id: int,
    company: CompanyUpdate,
    db: Session = Depends(get_db)
):
    updated_company = update_company(
        db,
        company_id,
        company
    )

    if not updated_company:
        return {"message": "Company not found"}

    return updated_company


@router.delete("/companies/{company_id}")
def remove_company(
    company_id: int,
    db: Session = Depends(get_db)
):
    deleted_company = delete_company(db, company_id)

    if not deleted_company:
        return {"message": "Company not found"}

    return deleted_company