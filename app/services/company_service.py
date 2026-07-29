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
    db_company = db.query(Company).filter(
        Company.id == company_id
    ).first()

    if not db_company:
        return None

    db_company.company_name = company.company_name
    db_company.industry = company.industry
    db_company.country = company.country

    db.commit()
    db.refresh(db_company)

    return db_company


def delete_company(db: Session, company_id: int):
    db_company = db.query(Company).filter(
        Company.id == company_id
    ).first()

    if not db_company:
        return None

    db.delete(db_company)
    db.commit()

    return {"message": "Company deleted successfully"}