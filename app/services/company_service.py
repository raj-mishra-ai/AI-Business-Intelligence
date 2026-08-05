import pandas as pd

from app.core.exceptions import (
    CompanyNotFoundException,
    CompanyAlreadyExistsException,
)

from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.company import Company
from app.schemas.company import CompanyCreate, CompanyUpdate


def create_company(db: Session, company: CompanyCreate):
    existing_company = (
        db.query(Company)
        .filter(Company.company_name == company.company_name)
        .first()
    )

    if existing_company:
        raise CompanyAlreadyExistsException()

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
    company = db.query(Company).filter(
        Company.id == company_id
    ).first()

    if not company:
        raise CompanyNotFoundException()

    return company


def update_company(
    db: Session,
    company_id: int,
    company: CompanyUpdate
):
    db_company = get_company_by_id(db, company_id)

    db_company.company_name = company.company_name
    db_company.industry = company.industry
    db_company.country = company.country

    db.commit()
    db.refresh(db_company)

    return db_company


def delete_company(db: Session, company_id: int):
    db_company = get_company_by_id(db, company_id)

    db.delete(db_company)
    db.commit()

    return {
        "message": "Company deleted successfully"
    }


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

def get_industry_analytics(db: Session):
    result = (
        db.query(
            Company.industry,
            func.count(Company.id).label("company_count")
        )
        .group_by(Company.industry)
        .all()
    )

    return [
        {
            "industry": row.industry,
            "company_count": row.company_count
        }
        for row in result
    ]  

def get_country_analytics(db: Session):
    result = (
        db.query(
            Company.country,
            func.count(Company.id).label("company_count")
        )
        .group_by(Company.country)
        .all()
    )

    return [
        {
            "country": row.country,
            "company_count": row.company_count
        }
        for row in result
    ]    

def get_dashboard_analytics(db: Session):
    return {
        "statistics": get_company_statistics(db),
        "industry_analytics": get_industry_analytics(db),
        "country_analytics": get_country_analytics(db)
    }   

def get_top_industries(db: Session):
    result = (
        db.query(
            Company.industry,
            func.count(Company.id).label("company_count")
        )
        .group_by(Company.industry)
        .order_by(func.count(Company.id).desc())
        .all()
    )

    return [
        {
            "industry": row.industry,
            "company_count": row.company_count
        }
        for row in result
    ]  

def get_top_countries(db: Session):
    result = (
        db.query(
            Company.country,
            func.count(Company.id).label("company_count")
        )
        .group_by(Company.country)
        .order_by(func.count(Company.id).desc())
        .all()
    )

    return [
        {
            "country": row.country,
            "company_count": row.company_count
        }
        for row in result
    ]  

def get_business_report(db: Session):
    return {
        "statistics": get_company_statistics(db),
        "top_industries": get_top_industries(db),
        "top_countries": get_top_countries(db),
        "industry_analytics": get_industry_analytics(db),
        "country_analytics": get_country_analytics(db)
    }           

import pandas as pd


def export_companies_to_csv(db: Session):
    companies = db.query(Company).all()

    data = []

    for company in companies:
        data.append({
            "ID": company.id,
            "Company Name": company.company_name,
            "Industry": company.industry,
            "Country": company.country
        })

    df = pd.DataFrame(data)

    file_path = "companies.csv"
    df.to_csv(file_path, index=False)

    return file_path   

def export_companies_to_excel(db: Session):
    companies = db.query(Company).all()

    data = []

    for company in companies:
        data.append({
            "ID": company.id,
            "Company Name": company.company_name,
            "Industry": company.industry,
            "Country": company.country
        })

    df = pd.DataFrame(data)

    file_path = "companies.xlsx"
    df.to_excel(file_path, index=False)

    return file_path     