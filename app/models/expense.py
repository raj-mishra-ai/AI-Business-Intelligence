from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from app.database.database import Base


class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    amount = Column(Float, nullable=False)
    category = Column(String(50), nullable=False)

    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="expenses")