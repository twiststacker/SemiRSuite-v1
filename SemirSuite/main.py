from fastapi import FastAPI
from SemirSuite.api import registry

app = FastAPI(title="SemirSuite Agent Registry API")

app.include_router(registry.router)
