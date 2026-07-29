from pydantic import BaseModel


class CompanyCreate(BaseModel):
    company_name: str
    industry: str
    country: str


class CompanyUpdate(BaseModel):
    company_name: str
    industry: str
    country: str


class CompanyResponse(BaseModel):
    id: int
    company_name: str
    industry: str
    country: str

    class Config:
        from_attributes = True