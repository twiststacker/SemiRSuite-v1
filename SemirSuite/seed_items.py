from app.db.session import SessionLocal
from app.db.models.item import Item

def seed_items():
    db = SessionLocal()
    items = [
        Item(name="IdeaForge", description="Generates video ideas using AI"),
        Item(name="ClipSlicer", description="Trims and edits video clips"),
        Item(name="TrendAnalyzer", description="Analyzes trending topics"),
    ]
    for item in items:
        if not db.query(Item).filter_by(name=item.name).first():
            db.add(item)
    db.commit()
    db.close()
    print("✅ Seeded items into database.")

if __name__ == "__main__":
    seed_items()