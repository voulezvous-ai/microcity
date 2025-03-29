from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from datetime import datetime

app = FastAPI()
db = []  # Simulação de banco de dados

class Message(BaseModel):
    id: int
    sender: str
    recipient: str
    subject: str
    content: str
    status: str = "unread"
    created_at: datetime = datetime.now()

@app.post("/inbox/send")
def send_message(msg: Message):
    db.append(msg)
    return {"message": "Enviado"}

@app.get("/inbox", response_model=List[Message])
def get_inbox(user: str):
    return [m for m in db if m.recipient == user and m.status != "archived"]

@app.patch("/inbox/{msg_id}/read")
def mark_read(msg_id: int):
    for m in db:
        if m.id == msg_id:
            m.status = "read"
            return {"message": "Marcada como lida"}
    raise HTTPException(status_code=404)

@app.patch("/inbox/{msg_id}/archive")
def archive_message(msg_id: int):
    for m in db:
        if m.id == msg_id:
            m.status = "archived"
            return {"message": "Arquivada"}
    raise HTTPException(status_code=404)
