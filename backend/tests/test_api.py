from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200


def test_list_prompts():
    response = client.get(
        "/prompts/",
        headers={"X-API-Key": "workbench-secret-key"},
    )

    assert response.status_code == 200


def test_invalid_prompt_creation():
    response = client.post(
        "/prompts/",
        json={
            "name": "Wrong Schema"
        },
        headers={"X-API-Key": "workbench-secret-key"},
    )

    assert response.status_code == 422


def test_invalid_api_key():
    response = client.get(
        "/prompts/",
        headers={"X-API-Key": "wrong-key"},
    )

    assert response.status_code == 401