from app.database import SessionLocal
from app.models import Item

def seed_items():
    db = SessionLocal()
    items = [
        Item(name="Cinematic Opener", description="Stylized intro sequence with dramatic transitions."),
        Item(name="Agent Core", description="Initial logic for agent orchestration."),
        Item(name="Metrics Tracker", description="Prometheus-compatible metrics endpoint."),
    ]
    for item in items:
        db.add(item)
    db.commit()
    db.close()
    print("✅ Seeded items successfully.")

if __name__ == "__main__":
    seed_items()