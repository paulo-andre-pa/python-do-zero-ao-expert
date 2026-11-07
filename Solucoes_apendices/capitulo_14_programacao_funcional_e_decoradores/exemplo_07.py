# Capítulo 14 — Programação funcional e decoradores
# Secção: Closures

def criar_contador():
    total = 0
    def incrementar(passo=1):
        nonlocal total
        total += passo
        return total
    return incrementar

contar = criar_contador()
contar(); contar(); print(contar(5))
