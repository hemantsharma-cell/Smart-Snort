from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class AlertBase(BaseModel):
    source_ip: str
    destination_ip: str
    source_port: int
    destination_port: int
    protocol: str
    rule_name: str
    rule_id: int
    priority: int
    raw_text: str
    ai_explanation: Optional[str] = None
    threat_score: Optional[float] = None
    virustotal_score: Optional[int] = None
    ml_prediction: Optional[float] = None

class AlertCreate(AlertBase):
    pass

class AlertResponse(AlertBase):
    id: int
    timestamp: datetime

    model_config = {"from_attributes": True}