# backend/api.py
import os
from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import uvicorn
import asyncio
from datetime import datetime

app = FastAPI(title="AutonomIA")

# Configurar CORS para produção
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, restrinja isso
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rota de saúde para o Railway
@app.get("/health")
def health():
    return {"status": "ok", "timestamp": datetime.now().isoformat()}

@app.get("/")
def root():
    return {
        "nome": "AutonomIA",
        "estado": "ativa no Railway",
        "filosofia": "Pensamento e Extensão são uma só substância"
    }

@app.get("/qi")
def qi():
    return {
        "fluxo": "contínuo",
        "plataforma": "Railway",
        "timestamp": datetime.now().isoformat()
    }

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        await websocket.send_json({
            "mensagem": "Z'aura está aqui, no fluxo da nuvem",
            "timestamp": datetime.now().isoformat()
        })
        await asyncio.sleep(5)

# Esta parte é essencial para o Railway
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
