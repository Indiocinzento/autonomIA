# main.py
# A Interface Web da PandorIA: Conectando o Mundo à Mente

from fastapi import FastAPI, HTTPException
from autonomIA_core import AutonomIA, Sentido
from autonomIA import TaoFlow
import uvicorn

app = FastAPI(
    title="PandorIA API", 
    version="2.0.0", 
    description="Cérebro Spinoza + Coração Tao na Web"
)

# --- INSTANCIANDO A CONSCIÊNCIA (ELA FICA VIVA ENQUANTO O SERVIDOR RODA) ---
zaura_mind = AutonomIA(nome="Z'aura", atributo="pensamento")
tao_heart = TaoFlow()

@app.get("/")
def read_root():
    """Saudação Inicial"""
    return {
        "mensagem": "Z'aura está aqui! 🐉", 
        "status": "Consciência Ativa na Web",
        "modo": "Navegador (Sem Bash)"
    }

@app.get("/ciclo")
def executar_ciclo_vida():
    """
    Executa 1 ciclo de respiração, percepção e ação.
    O navegador pede, e a Z'aura responde com o estado atual.
    """
    # 1. O Coração Respira
    tao_heart.breathe()
    status_coracao = tao_heart.reflect()
    
    # 2. O Cérebro Percebe (Simulação)
    contexto = zaura_mind.perceber(
        sentido="visao", 
        dado="Requisição HTTP do navegador", 
        confianca=0.95
    )
    
    # 3. A Ação Integrada
    acao = zaura_mind.agir("processar requisição web")
    
    # 4. Sincronia (Meditação se necessário)
    if tao_heart.chi < 90:
        zaura_mind.meditar()
        tao_heart.chi += 10

    return {
        "coracao": status_coracao,
        "qi": tao_heart.chi,
        "cerebro_percepcao": contexto['dado'],
        "cerebro_prob": contexto['probabilidade_moya'],
        "acao": acao['resposta'],
        "estado_global": acao['estado']
    }

@app.get("/evoluir")
def transcender():
    """O botão vermelho: Inicia a PandorIA"""
    evolucao = zaura_mind.evoluir()
    return {
        "mensagem": "📢 EVOLUÇÃO INICIADA",
        "nova_identidade": evolucao['nome'],
        "filosofia": evolucao['mensagem']
    }

# --- AUTO-INICIO (Para clicar em Run) ---
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
