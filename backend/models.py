from sqlalchemy import Column, Integer, String, DateTime, Float
from datetime import datetime
from database import Base

class AlertModel(Base):
    __tablename__ = "alerts"
    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    source_ip = Column(String)
    destination_ip = Column(String)
    source_port = Column(Integer)
    destination_port = Column(Integer)
    protocol = Column(String)
    rule_name = Column(String)
    rule_id = Column(Integer)
    priority = Column(Integer)
    raw_text = Column(String)
    ai_explanation = Column(String, nullable=True)
    threat_score = Column(Float, nullable=True)
    virustotal_score = Column(Integer, nullable=True)
    ml_prediction = Column(Float, nullable=True)