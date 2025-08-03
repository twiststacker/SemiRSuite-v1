from sqlalchemy import Column, Integer, String
from src.database import Base
from pydantic import BaseModel, Field

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(String)

# 🔹 Pydantic models
class ItemCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=255)
    description: str

class ItemResponse(BaseModel):
    id: int
    name: str
    description: str

    class Config:
        orm_mode = True