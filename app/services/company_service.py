from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.company import Company
from app.schemas.company import CompanyCreate, CompanyUpdate


def create_company(db: Session, company: CompanyCreate):
    new_company = Company(
        company_name=company.company_name,
        industry=company.industry,
        country=company.country
    )

    db.add(new_company)
    db.commit()
    db.refresh(new_company)

    return new_company


def get_companies(db: Session):
    return db.query(Company).all()


def get_company_by_id(db: Session, company_id: int):
    return db.query(Company).filter(
        Company.id == company_id
    ).first()


def update_company(
    db: Session,
    company_id: int,
    company: CompanyUpdate
):
    existing_company = get_company_by_id(db, company_id)

    if not existing_company:
        return None

    existing_company.company_name = company.company_name
    existing_company.industry = company.industry
    existing_company.country = company.country

    db.commit()
    db.refresh(existing_company)

    return existing_company


def delete_company(db: Session, company_id: int):
    company = get_company_by_id(db, company_id)

    if not company:
        return None

    db.delete(company)
    db.commit()

    return company


def get_company_summary(db: Session):
    total_companies = db.query(Company).count()

    return {
        "total_companies": total_companies
    }


def search_company(db: Session, company_name: str):
    return db.query(Company).filter(
        Company.company_name.ilike(f"%{company_name}%")
    ).all()


def filter_by_industry(db: Session, industry: str):
    return db.query(Company).filter(
        Company.industry == industry
    ).all()


def filter_by_country(db: Session, country: str):
    return db.query(Company).filter(
        Company.country == country
    ).all()


def sort_companies(db: Session, order: str = "asc"):
    if order.lower() == "desc":
        return db.query(Company).order_by(
            Company.company_name.desc()
        ).all()

    return db.query(Company).order_by(
        Company.company_name.asc()
    ).all()


def get_companies_paginated(
    db: Session,
    limit: int = 10,
    offset: int = 0
):
    return (
        db.query(Company)
        .offset(offset)
        .limit(limit)
        .all()
    )


def get_company_statistics(db: Session):
    total_companies = db.query(Company).count()

    total_industries = db.query(
        func.count(func.distinct(Company.industry))
    ).scalar()

    total_countries = db.query(
        func.count(func.distinct(Company.country))
    ).scalar()

    average_companies_per_country = (
        total_companies / total_countries
        if total_countries
        else 0
    )

    return {
        "total_companies": total_companies,
        "total_industries": total_industries,
        "total_countries": total_countries,
        "average_companies_per_country": round(
            average_companies_per_country,
            2
        )
    }