from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Smart Fleet Maintenance API!"}

def test_register_equipment():
    response = client.post("/equipment/", json={
        "model": "Tractor X",
        "purchase_date": "2023-01-01",
        "usage_hours": 100
    })
    assert response.status_code == 201
    assert response.json()["model"] == "Tractor X"

def test_get_equipment():
    response = client.get("/equipment/1")
    assert response.status_code == 200
    assert response.json()["model"] == "Tractor X"  # Assuming this is the first equipment registered

def test_service_logging():
    response = client.post("/equipment/1/service/", json={
        "service_date": "2023-06-01",
        "description": "Oil change"
    })
    assert response.status_code == 201
    assert response.json()["description"] == "Oil change"