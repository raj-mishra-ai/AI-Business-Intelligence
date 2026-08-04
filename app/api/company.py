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
    sort_companies,
    get_companies_paginated,
    get_company_statistics,
    get_industry_analytics,
    get_country_analytics,
    get_dashboard_analytics,
    get_top_industries,
    get_top_countries,
    get_business_report,
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


@router.get("/companies/sort")
def sort_company_list(
    order: str = "asc",
    db: Session = Depends(get_db)
):
    return sort_companies(db, order)


@router.get("/companies/paginated")
def read_companies_paginated(
    limit: int = 10,
    offset: int = 0,
    db: Session = Depends(get_db)
):
    return get_companies_paginated(db, limit, offset)


@router.get("/companies/statistics")
def company_statistics(
    db: Session = Depends(get_db)
):
    return get_company_statistics(db)


@router.get("/companies/analytics/industry")
def industry_analytics(
    db: Session = Depends(get_db)
):
    return get_industry_analytics(db)


@router.get("/companies/analytics/country")
def country_analytics(
    db: Session = Depends(get_db)
):
    return get_country_analytics(db)


@router.get("/companies/dashboard")
def dashboard_analytics(
    db: Session = Depends(get_db)
):
    return get_dashboard_analytics(db)


@router.get("/companies/reports/top-industries")
def top_industries_report(
    db: Session = Depends(get_db)
):
    return get_top_industries(db)


@router.get("/companies/reports/top-countries")
def top_countries_report(
    db: Session = Depends(get_db)
):
    return get_top_countries(db)


@router.get("/companies/reports/business")
def business_report(
    db: Session = Depends(get_db)
):
    return get_business_report(db)


# ⚠️ Is endpoint ko hamesha sabse last GET endpoint rakho
@router.get("/companies/{company_id}")
def read_company(
    company_id: int,
    db: Session = Depends(get_db)
):
    return get_company_by_id(db, company_id)


@router.put("/companies/{company_id}")
def edit_company(
    company_id: int,
    company: CompanyUpdate,
    db: Session = Depends(get_db)
):
    return update_company(
        db,
        company_id,
        company
    )


@router.delete("/companies/{company_id}")
def remove_company(
    company_id: int,
    db: Session = Depends(get_db)
):
    return delete_company(db, company_id)