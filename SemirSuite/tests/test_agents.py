from fastapi.testclient import TestClient
import pytest

def test_ideaforge_agent(client: TestClient):
    response = client.post(
        "/api/v1/generate-ideas",
        json={"prompt": "Create a video tutorial on AI"}
    )
    assert response.status_code == 200
    data = response.json()
    assert len(data["ideas"]) > 0