# Capítulo 4 — Decisões: if, elif, else e match
# Secção: A instrução if

saldo = 80
levantamento = 120
if levantamento <= saldo:
    saldo -= levantamento
    print(f"Levantou {levantamento} €. Saldo: {saldo} €")
else:
    print("Saldo insuficiente.")
