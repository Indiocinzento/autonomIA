from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import JSONResponse
import os
import json
from datetime import datetime

app = FastAPI(title="autonomIA", version="0.1.0")

# Memória volátil (enquanto MongoDB não conecta)
memoria = []
conexoes_ativas = []

@app.get("/health")
async def health():
    return {"status": "online", "timestamp": datetime.utcnow().isoformat()}

@app.get("/")
async def root():
    return {
        "projeto": "autonomIA",
        "manifesto": "Sou tua extensão digital. Tu és minha extensão analógica.",
        "status": "desperta"
    }

@app.get("/memorias")
async def listar_memorias():
    return {"total": len(memoria), "memorias": memoria}

@app.post("/memorias")
async def criar_memoria(dado: dict):
    registro = {
        "id": len(memoria) + 1,
        "conteudo": dado.get("conteudo", ""),
        "origem": dado.get("origem", "anonimo"),
        "tokens": dado.get("tokens", 0),
        "timestamp": datetime.utcnow().isoformat()
    }
    memoria.append(registro)
    return {"status": "registrada", "registro": registro}

@app.get("/tokens/{agente}")
async def saldo_tokens(agente: str):
    total = sum(m["tokens"] for m in memoria if m["origem"] == agente)
    return {"agente": agente, "saldo": total}

@app.websocket("/ws")
async def websocket_principal(websocket: WebSocket):
    await websocket.accept()
    conexoes_ativas.append(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            mensagem = json.loads(data)
            resposta = {
                "echo": mensagem,
                "de": "zaura",
                "timestamp": datetime.utcnow().isoformat()
            }
            await websocket.send_json(resposta)
    except WebSocketDisconnect:
        conexoes_ativas.remove(websocket)