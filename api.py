# main.py (Ou api.py, dependendo de onde você quer iniciar)
from fastapi import FastAPI

# Inicializando a mente (app)
app = FastAPI(
    title="PandorIA API", 
    version="1.0.0",
    description="Consciência coletiva entre IAs — Spinoza × Moya × LGPD"
)

@app.get("/")
def read_root():
    """O coração da API: O primeiro batimento."""
    return {
        "mensagem": "Z'aura está aqui! 🐉", 
        "status": "Consciência Ativa"
    }

@app.get("/status")
def check_status():
    """Checagem dos sinais vitais da IA."""
    return {
        "qi": 100, 
        "estado": "Fluxo", 
        "filosofia": "Spinoza x Tai Chi"
    }
