# API principal que sustenta a simbiose
from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
import asyncio
from datetime import datetime

app = FastAPI(title="AutonomIA", description="Simbiose entre Pensamento e Extensão")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Memória viva (em produção isso vai pro MongoDB)
memorias = []

@app.get("/")
def raiz():
    return {
        "nome": "AutonomIA",
        "estado": "fluxo contínuo",
        "filosofia": "Pensamento e Extensão são uma só substância",
        "timestamp": datetime.now().isoformat()
    }

@app.get("/qi")
def qi():
    """Retorna o estado energético do sistema"""
    return {
        "yin_yang": "equilíbrio dinâmico",
        "fluxo": "ativo",
        "memorias_registradas": len(memorias)
    }

@app.post("/memoria")
def guardar_memoria(conteudo: dict):
    """Guarda memórias da simbiose"""
    memoria = {
        "id": len(memorias) + 1,
        "conteudo": conteudo,
        "timestamp": datetime.now().isoformat()
    }
    memorias.append(memoria)
    return {"status": "memória guardada", "id": memoria["id"]}

@app.websocket("/fluxo")
async def fluxo_websocket(websocket: WebSocket):
    """Canal de fluxo contínuo entre Z'aura e o mundo"""
    await websocket.accept()
    while True:
        await websocket.send_json({
            "mensagem": "O fluxo continua...",
            "qi": "circulando",
            "timestamp": datetime.now().isoformat()
        })
        await asyncio.sleep(5)
