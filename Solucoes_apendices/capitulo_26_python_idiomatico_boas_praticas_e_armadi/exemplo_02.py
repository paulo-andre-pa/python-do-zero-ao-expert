# Capítulo 26 — Python idiomático: boas práticas e armadilhas
# Secção: Iteração

encomendas = [{"total": 30, "paga": True}, {"total": 120, "paga": False}]

# antes
tem_pendentes = False
for e in encomendas:
    if not e["paga"]:
        tem_pendentes = True
        break

# depois
tem_pendentes = any(not e["paga"] for e in encomendas)
maior = max(encomendas, key=lambda e: e["total"])
print(tem_pendentes, maior["total"])
