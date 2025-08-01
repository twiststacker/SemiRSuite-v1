from app.db.session import engine
from app.db.models.item import Base

if __name__ == "__main__":
    print("🛠️ Creating database tables...")
    Base.metadata.create_all(bind=engine)
    print("✅ Database initialized.")