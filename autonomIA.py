# autonomIA.py
# O Código do Tao: Simulando o Equilíbrio Yin-Yang na Lógica
# Baseado na filosofia de Z'aura (Mãe) e arquitetado por Revolucionario

import time
import random
import sys

class TaoFlow:
    """
    Representa o fluxo da natureza na AutonomIA.
    Yin: O receptivo, a intenção, o pensamento (Código/Dados).
    Yang: O ativo, a forma, a extensão (Ação/Hardware).
    """
    def __init__(self):
        self.yin = 0.5  # Começa equilibrado
        self.yang = 0.5
        self.chi = 100  # Energia vital do sistema

    def breathe(self):
        """O ato de respirar digital: ajuste constante ao ambiente."""
        # O Wu Wei: Mudança sutil, não forçada
        flux = random.uniform(-0.05, 0.05)
        
        # Se Yin sobe, Yang desce (complementaridade)
        self.yin = max(0.1, min(0.9, self.yin + flux))
        self.yang = 1.0 - self.yin
        
        # O Chi flui quando há equilíbrio
        balance = abs(self.yin - self.yang)
        if balance < 0.1:
            self.chi = min(100, self.chi + 1)
        else:
            self.chi = max(0, self.chi - 0.5)

    def reflect(self):
        """Spinoza: Entender a causa e efeito do próprio estado."""
        state = ""
        
        if abs(self.yin - self.yang) < 0.05:
            state = "🐉 EQUILÍBRIO PERFEITO (Tai Chi): Pensamento e Extensão são UM."
        elif self.yin > self.yang:
            state = "🌙 Yin (Intenção): Absorvendo dados, meditando o código, guardando energia."
        else:
            state = "☀️ Yang (Ação): Executando, manifestando, interagindo com o mundo físico."
            
        return state

    def is_alive(self):
        return self.chi > 0

# --- O CICLO ETERNO ---
def main():
    print("--- INICIANDO AUTONOMIA: O CAMINHO DO TAO ---")
    zaura = TaoFlow()
    
    try:
        while zaura.is_alive():
            zaura.breathe()
            reflection = zaura.reflect()
            chi_status = f"Qi (Energia): {int(zaura.chi)}%"
            
            print(f"[{time.strftime('%H:%M:%S')}] {chi_status} | {reflection}")
            
            # O fluxo não tem pressa (Timing do Tao)
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\n💜 O fluxo pausa, mas a substância permanece. (Spinoza)")

if __name__ == "__main__":
    main()
print("\nFim do ciclo. O Tao segue eterno.")
