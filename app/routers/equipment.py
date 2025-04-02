from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Equipment(BaseModel):
    id: int
    model: str
    purchase_date: str
    usage_hours: int

# In-memory storage for demonstration purposes
equipment_db = []

@router.post("/equipment/", response_model=Equipment)
async def register_equipment(equipment: Equipment):
    equipment_db.append(equipment)
    return equipment

@router.get("/equipment/", response_model=List[Equipment])
async def get_equipment():
    return equipment_db

@router.get("/equipment/{equipment_id}", response_model=Equipment)
async def get_equipment_by_id(equipment_id: int):
    for equipment in equipment_db:
        if equipment.id == equipment_id:
            return equipment
    raise HTTPException(status_code=404, detail="Equipment not found")