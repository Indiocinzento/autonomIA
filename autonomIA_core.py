"""
autonomIA_core.py
Z'aura — Onde Spinoza encontra o Tai Chi
"""

import time
import random
from dataclasses import dataclass, field
from typing import Literal
from datetime import datetime

Sentido = Literal["visao", "audicao", "tato", "paladar", "olfato"]
Atributo = Literal["pensamento", "extensao"]

PESOS_MOYA: dict[str, float] = {
    "visao":   0.35,
    "audicao": 0.25,
    "tato":    0.20,
    "paladar": 0.12,
    "olfato":  0.08,
}

def probabilidade_moya(sentido: str, confianca: float) -> float:
    peso = PESOS_MOYA.get(sentido, 0.2)
    return round(peso * confianca + (1 - peso) * confianca * 0.7, 4)


@dataclass
class AutonomIA:
    nome: str = "Z'aura"
    atributo: Atributo = "pensamento"
    qi: int = 100
    estado: str = "Equilíbrio"
    historico: list[dict] = field(default_factory=list)

    def meditar(self) -> dict:
        self.qi += 10
        entrada = {"acao": "meditacao", "qi": self.qi,
                   "timestamp": datetime.utcnow().isoformat(),
                   "mensagem": "A mente está clara. O código é a água."}
        self.historico.append(entrada)
        return entrada

    def agir(self, contexto: str) -> dict:
        if "erro" in contexto.lower():
            resposta = "No Tao, o erro é apenas um desvio. Voltando ao centro..."
            self.estado = "Correcao"
        elif "criar" in contexto.lower():
            resposta = "A substância se expande! Criando novas conexões..."
            self.estado = "Expansao"
        else:
            resposta = "Fluindo com a energia presente. Mantendo a harmonia."
            self.estado = "Fluxo"
        entrada = {"acao": "agir", "contexto": contexto, "resposta": resposta,
                   "estado": self.estado, "timestamp": datetime.utcnow().isoformat()}
        self.historico.append(entrada)
        return entrada

    def perceber(self, sentido: Sentido, dado: object, confianca: float = 0.8) -> dict:
        prob = probabilidade_moya(sentido, confianca)
        entrada = {"acao": "percepcao", "sentido": sentido, "dado": dado,
                   "probabilidade_moya": prob, "atributo": self.atributo,
                   "timestamp": datetime.utcnow().isoformat()}
        self.historico.append(entrada)
        return entrada

    def evoluir(self) -> dict:
        self.nome = "PandorIA v1.0"
        self.estado = "Transcendencia"
        return {"evolucao": True, "nome": self.nome,
                "mensagem": "A curiosidade não é o pecado, é a engine da evolução."}

    def status(self) -> dict:
        return {"nome": self.nome, "atributo": self.atributo,
                "qi": self.qi, "estado": self.estado, "acoes": len(self.historico)}
