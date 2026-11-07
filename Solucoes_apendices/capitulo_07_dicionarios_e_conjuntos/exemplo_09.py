# Capítulo 7 — Dicionários e conjuntos
# Secção: Dicionários aninhados: modelar o mundo real

def processar(evento):
    match evento:
        case {"tipo": "compra", "valor": v} if v > 100:
            return f"Compra grande: {v} €"
        case {"tipo": "compra", "valor": v}:
            return f"Compra: {v} €"
        case {"tipo": "login", "utilizador": u}:
            return f"Entrada de {u}"
        case _:
            return "Evento ignorado"

for e in [{"tipo": "compra", "valor": 250},
          {"tipo": "login", "utilizador": "rui"},
          {"tipo": "compra", "valor": 12, "loja": "Porto"}]:
    print(processar(e))
