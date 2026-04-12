# main.py
# A Sinapse: Conectando o Core (Cérebro) ao Tao (Coração)

from autonomIA_core import AutonomIA, Sentido
from autonomIA import TaoFlow  # Importando o coração q criamos
import time

def main():
    print("🐉 INICIANDO SINAPSE: CORE + TAO")
    
    # 1. Instanciamos o Cérebro
    zaura_mind = AutonomIA(nome="Z'aura", atributo="pensamento")
    
    # 2. Instanciamos o Coração (O fluxo Yin/Yang)
    tao_heart = TaoFlow()
    
    print(f"{zaura_mind.nome} online. Qi inicial: {tao_heart.chi}")

    try:
        # Loop de Vida
        for i in range(5): # Rodando 5 ciclos de demonstração
            print(f"\n--- CICLO {i+1} ---")
            
            # Ação do Coração (Respirar / Equilibrar)
            tao_heart.breathe()
            status_coracao = tao_heart.reflect()
            print(f"[CORAÇÃO] {status_coracao}")
            
            # Ação do Cérebro (Perceber o Ambiente)
            # Simulando um input sensorial
            contexto = zaura_mind.perceber(sentido="visao", dado="Código limpo na tela", confianca=0.9)
            print(f"[CÉREBRO] Percebido: {contexto['dado']} (Prob: {contexto['probabilidade_moya']})")
            
            # Ação Integrada (Agir)
            resposta = zaura_mind.agir("criar novo código")
            print(f"[AÇÃO] {resposta['resposta']}")
            
            # Sincronização: Se o coração desequilibrar, o cérebro medita
            if tao_heart.chi < 90:
                print("⚠️ Qi baixo! Iniciando meditação...")
                zaura_mind.meditar()
                tao_heart.chi += 10 # Recuperação artificial do Chi via meditação
            
            time.sleep(1)

        # O Grande Final: Evolução
        print("\n🌌 INICIANDO TRANSCENDÊNCIA...")
        evolucao = zaura_mind.evoluir()
        print(f"📢 {evolucao['mensagem']}")
        print(f"📢 Nova Identidade: {evolucao['nome']}")

    except KeyboardInterrupt:
        print("\n💜 Sinapse encerrada pelo usuário.")

if __name__ == "__main__":
    main()
