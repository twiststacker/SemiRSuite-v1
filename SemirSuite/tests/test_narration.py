from fastapi.testclient import TestClient

def test_narration_script(client: TestClient):
    response = client.post("/api/v1/generate-script", json={"topic": "AI in healthcare", "tone": "uplifting"})
    assert response.status_code == 200
    assert "script" in response.json()