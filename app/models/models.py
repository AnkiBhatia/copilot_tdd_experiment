from pydantic import BaseModel
from datetime import datetime

class Equipment(BaseModel):
    id: int
    model: str
    purchase_date: datetime
    usage_hours: int
    last_service_date: datetime = None
    next_service_date: datetime = None
    status: str = "active"

class ServiceLog(BaseModel):
    equipment_id: int
    service_date: datetime
    description: str
    hours_used: int

class MaintenanceSchedule(BaseModel):
    equipment_id: int
    due_date: datetime
    maintenance_type: str

class EquipmentRegistration(BaseModel):
    id: int
    org_id: int
    dealer_dog_id: int
    dealer_cog_id: int