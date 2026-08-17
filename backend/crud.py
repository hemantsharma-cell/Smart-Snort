from sqlalchemy.orm import Session
import models, schemas

def get_alerts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.AlertModel).offset(skip).limit(limit).all()

def create_alert(db: Session, alert: schemas.AlertCreate):
    db_alert = models.AlertModel(**alert.model_dump())
    db.add(db_alert)
    db.commit()
    db.refresh(db_alert)
    return db_alert