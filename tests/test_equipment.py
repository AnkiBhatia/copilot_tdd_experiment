import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_register_equipment():
    response = client.post("/equipment/", json={
        "model": "Tractor",
        "purchase_date": "2023-01-01",
        "usage_hours": 100
    })
    assert response.status_code == 201
    assert response.json()["model"] == "Tractor"

def test_get_equipment():
    response = client.get("/equipment/1")
    assert response.status_code == 200
    assert "model" in response.json()

def test_update_equipment():
    response = client.put("/equipment/1", json={
        "model": "Updated Tractor",
        "purchase_date": "2023-01-01",
        "usage_hours": 150
    })
    assert response.status_code == 200
    assert response.json()["model"] == "Updated Tractor"

def test_delete_equipment():
    response = client.delete("/equipment/1")
    assert response.status_code == 204

def test_get_nonexistent_equipment():
    response = client.get("/equipment/999")
    assert response.status_code == 404