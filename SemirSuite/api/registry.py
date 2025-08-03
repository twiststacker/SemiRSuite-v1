from fastapi import APIRouter, HTTPException
import toml
import os

router = APIRouter()
REGISTRY_PATH = os.path.join("semirsuite", "configs", "agent_registry.toml")

def load_registry():
    try:
        return toml.load(REGISTRY_PATH)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to load registry: {str(e)}")

@router.get("/agents")
def list_agents():
    return load_registry()

@router.get("/agents/{agent_name}")
def get_agent(agent_name: str):
    registry = load_registry()
    agent = registry.get(agent_name)
    if not agent:
        raise HTTPException(status_code=404, detail="Agent not found")
    return agent