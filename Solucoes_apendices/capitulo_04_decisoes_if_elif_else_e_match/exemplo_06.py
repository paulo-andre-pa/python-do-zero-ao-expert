# Capítulo 4 — Decisões: if, elif, else e match
# Secção: Condições compostas

def calcular_desconto(valor, cliente_vip, cupao):
    if valor <= 0:
        return 0                     # guarda: nada a descontar
    if cliente_vip:
        return valor * 0.15
    if cupao == "BEMVINDO":
        return valor * 0.10
    return 0

print(calcular_desconto(200, False, "BEMVINDO"))
print(calcular_desconto(200, True, None))
