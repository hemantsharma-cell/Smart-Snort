from fastapi import FastAPI, Depends, WebSocket, WebSocketDisconnect
import models, database, schemas, crud
from sqlalchemy.orm import Session
from threat_intel import get_abuseipdb_score, get_virustotal_score
from ai_explainer import get_ai_explanation
import requests, json


models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: dict):
        for connection in self.active_connections:
            await connection.send_json(message)

manager = ConnectionManager()

@app.get("/")
def read_root():
    return {"status": "success", "message": "Hello from the snort backend"}

@app.get("/alerts/", response_model=list[schemas.AlertResponse])
def read_alerts(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    return crud.get_alerts(db, skip=skip, limit=limit)

@app.post("/alerts/", response_model=schemas.AlertResponse)
async def create_alert(alert: schemas.AlertCreate, db: Session = Depends(database.get_db)):
    ai_text = get_ai_explanation(alert.rule_name, alert.raw_text)
    ip_score = get_abuseipdb_score(alert.source_ip)
    vt_votes = get_virustotal_score(alert.source_ip)
    alert.ai_explanation = ai_text
    alert.threat_score = ip_score
    alert.virustotal_score = vt_votes
    saved_alert = crud.create_alert(db=db, alert=alert)
    alert_dict = {k:v for k,v in saved_alert.__dict__.items() if not k.startswith('_') }
    await manager.broadcast(alert_dict)
    return saved_alert

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        manager.disconnect(websocket)