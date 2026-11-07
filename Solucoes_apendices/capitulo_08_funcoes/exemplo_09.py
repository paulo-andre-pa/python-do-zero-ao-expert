# Capítulo 8 — Funções
# Secção: Âmbito das variáveis

TAXA = 0.23            # global

def calcular(valor):
    resultado = valor * (1 + TAXA)   # 'resultado' é local
    return resultado

print(calcular(10))
print("resultado" in globals())
