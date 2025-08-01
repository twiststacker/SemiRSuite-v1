from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base, SessionLocal
from routes.items import router as items_router

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="SemirSuite API",
    description="An AI-Powered Video Creation Framework",
    version="1.0"
)

# CORS (optional)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(items_router, prefix="/items", tags=["Items"])