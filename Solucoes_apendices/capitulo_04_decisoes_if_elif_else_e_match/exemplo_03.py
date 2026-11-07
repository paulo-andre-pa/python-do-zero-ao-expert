# Capítulo 4 — Decisões: if, elif, else e match
# Secção: A instrução if

def classificar(nota):
    if nota >= 18:
        return "Excelente"
    elif nota >= 14:
        return "Bom"
    elif nota >= 10:
        return "Suficiente"
    else:
        return "Insuficiente"

for n in (19, 15, 10, 7):
    print(n, classificar(n))
