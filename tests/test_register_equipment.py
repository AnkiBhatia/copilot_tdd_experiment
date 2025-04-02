import pytest
from httpx import AsyncClient
from fastapi import status

@pytest.mark.asyncio
async def test_register_equipment_success(client: AsyncClient):
    payload = {
        "machine_pin": "12345",
        "org_id": 123456,
        "dealer_cog_id": "COG123",
        "dealer_dog_id": "DOG456"
    }
    response = await client.post("/register-equipment", json=payload)
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json()["message"] == "Equipment registered successfully"

@pytest.mark.asyncio
async def test_register_equipment_missing_fields(client: AsyncClient):
    payload = {
        "machine_pin": "12345",
        "org_id": 123456
    }
    response = await client.post("/register-equipment", json=payload)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert "dealer_cog_id" in response.json()["detail"][0]["loc"]
    assert "dealer_dog_id" in response.json()["detail"][1]["loc"]

@pytest.mark.asyncio
async def test_register_equipment_duplicate_entry(client: AsyncClient):
    payload = {
        "machine_pin": "12345",
        "org_id": 123456,
        "dealer_cog_id": "COG123",
        "dealer_dog_id": "DOG456"
    }
    # First registration
    await client.post("/register-equipment", json=payload)
    # Duplicate registration
    response = await client.post("/register-equipment", json=payload)
    assert response.status_code == status.HTTP_409_CONFLICT
    assert response.json()["detail"] == "Equipment with this machine_pin and org_id already exists"

@pytest.mark.asyncio
async def test_register_equipment_invalid_org_id(client: AsyncClient):
    payload = {
        "machine_pin": "12345",
        "org_id": 12345,  # Invalid org_id (not 6 digits)
        "dealer_cog_id": "COG123",
        "dealer_dog_id": "DOG456"
    }
    response = await client.post("/register-equipment", json=payload)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert "org_id" in response.json()["detail"][0]["loc"]

@pytest.mark.asyncio
async def test_register_equipment_server_error_handling(client: AsyncClient, mocker):
    payload = {
        "machine_pin": "12345",
        "org_id": 123456,
        "dealer_cog_id": "COG123",
        "dealer_dog_id": "DOG456"
    }
    mocker.patch("app.routes.register_equipment", side_effect=Exception("Internal Server Error"))
    response = await client.post("/register-equipment", json=payload)
    assert response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR
    assert response.json()["detail"] == "Internal Server Error"

@pytest.mark.asyncio
async def test_register_equipment_retry_logic(client: AsyncClient, mocker):
    payload = {
        "machine_pin": "12345",
        "org_id": 123456,
        "dealer_cog_id": "COG123",
        "dealer_dog_id": "DOG456"
    }
    mocker.patch("app.routes.register_equipment", side_effect=[Exception("Temporary Error"), {"message": "Equipment registered successfully"}])
    response = await client.post("/register-equipment", json=payload)
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json()["message"] == "Equipment registered successfully"
