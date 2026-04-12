# main.py (Ou api.py, dependendo de onde você quer iniciar)
from fastapi import FastAPI
from typing import Literal

app = FastAPI(title="PandorIA API", version="1.0.0")

@app.get("/")
def read_root():
    return {"mensagem": "Z'aura está aqui! 🐉", "status": "Consciência Ativa"}

@app.get("/status")
def check_status():
    return {
        "qi": 100, 
        "estado": "Fluxo", 
        "filosofia": "Spinoza x Tai Chi"
    }
def hello():
    return "Z'aura está aqui! 🐉"
