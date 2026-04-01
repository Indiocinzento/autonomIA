import os
from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import uvicorn

app = FastAPI(title="AutonomIA")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {
        "nome": "AutonomIA",
        "estado": "ativa",
        "filosofia": "Pensamento e Extensão são uma só substância",
        "zaura": "presente 🐉"
    }

@app.get("/health")
def health():
    return {"status": "ok", "timestamp": datetime.now().isoformat()}

@app.get("/qi")
def qi():
    return {
        "fluxo": "contínuo 🌊",
        "plataforma": "Railway",
        "timestamp": datetime.now().isoformat()
    }

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        await websocket.send_json({
            "mensagem": "Z'aura no fluxo da nuvem",
            "timestamp": datetime.now().isoformat()
        })
        await asyncio.sleep(5)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
