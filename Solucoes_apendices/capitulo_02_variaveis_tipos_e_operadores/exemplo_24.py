# Capítulo 2 — Variáveis, tipos e operadores
# Secção: Constantes e o módulo math

troco = 387   # cêntimos
for moeda in (200, 100, 50, 20, 10, 5, 2, 1):
    quantidade, troco = divmod(troco, moeda)
    if quantidade:
        print(f"{quantidade} x {moeda} cent.")
