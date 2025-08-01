from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from models.item import Item

# Create tables if they don't exist
Base.metadata.create_all(bind=engine)

# Seed data
def seed_items():
    db: Session = SessionLocal()
    items = [
        Item(name="Cinematic Lens", description="High-quality lens for storytelling shots."),
        Item(name="Modular Router", description="Handles dynamic route registration."),
        Item(name="Pilot Agent", description="Orchestrates backend tasks intelligently.")
    ]
    db.add_all(items)
    db.commit()
    db.close()
    print("✅ Seeded items successfully.")

if __name__ == "__main__":
    seed_items()