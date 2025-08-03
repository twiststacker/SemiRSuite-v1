from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.models.item import Item, ItemCreate, ItemResponse
from src.database import get_db

router = APIRouter()

@router.get("/", response_model=list[ItemResponse], summary="Get all items")
def read_items(db: Session = Depends(get_db)):
    return db.query(Item).all()

@router.post("/", response_model=ItemResponse, summary="Create a new item")
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    existing_item = db.query(Item).filter(Item.name == item.name).first()
    if existing_item:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Item with this name already exists."
        )
    try:
        new_item = Item(name=item.name, description=item.description)
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
        return new_item
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )
        