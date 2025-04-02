from datetime import datetime, timedelta
from typing import List, Optional
from app.models import Equipment
import random

class MaintenanceService:
    def __init__(self, equipment: List[Equipment]):
        self.equipment = equipment

    def predict_maintenance_due(self, equipment_id: int) -> Optional[datetime]:
        equipment_item = next((eq for eq in self.equipment if eq.id == equipment_id), None)
        if not equipment_item:
            return None
        
        # Example logic: Predict maintenance due in 100 hours of usage
        usage_threshold = 100
        if equipment_item.usage_hours >= usage_threshold:
            return datetime.now() + timedelta(days=30)  # Maintenance due in 30 days
        return None

    def log_service(self, equipment_id: int, service_details: str) -> bool:
        equipment_item = next((eq for eq in self.equipment if eq.id == equipment_id), None)
        if not equipment_item:
            return False
        
        # Simulate logging service
        equipment_item.service_records.append({
            "date": datetime.now(),
            "details": service_details
        })
        return True

    def get_service_records(self, equipment_id: int) -> List[dict]:
        equipment_item = next((eq for eq in self.equipment if eq.id == equipment_id), None)
        if not equipment_item:
            return []
        
        return equipment_item.service_records

# Example usage
# service = MaintenanceService(equipment_list)
# service.predict_maintenance_due(equipment_id)
# service.log_service(equipment_id, "Oil change")
# service.get_service_records(equipment_id)