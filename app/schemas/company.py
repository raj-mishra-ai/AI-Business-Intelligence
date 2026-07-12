from pydantic import BaseModel


class CompanyCreate(BaseModel):
    company_name: str
    industry: str
    country: str


class CompanyResponse(CompanyCreate):
    id: int

    class Config:
        from_attributes = True