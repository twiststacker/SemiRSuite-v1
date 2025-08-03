from fastapi import FastAPI
from semirsuite.routes import items
from semirsuite.app.db.models.item import Base
from semirsuite.app.db.session import engine
from semirsuite.seed_items import seed_items

Base.metadata.create_all(bind=engine)
seed_items()

app = FastAPI(
    title="SemirSuite API",
    description="Modular backend for scalable systems",
    version="1.0.0"
)

app.include_router(items.router, prefix="/items", tags=["Items"])