from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from database import Base

# SQLAlchemy model
class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)

# Pydantic model for creating an item
class ItemCreate(BaseModel):
    name: str
    description: str

# Pydantic model for returning an item
class ItemResponse(BaseModel):
    id: int
    name: str
    description: str

    model_config = {
        "from_attributes": True  # replaces orm_mode in Pydantic v2
    }