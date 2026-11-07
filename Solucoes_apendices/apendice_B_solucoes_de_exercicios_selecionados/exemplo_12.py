# Apêndice B — Soluções de exercícios selecionados
# Secção: Capítulo 8 — Funções

def luhn_valido(numero: str) -> bool:
    digitos = [int(c) for c in numero if c.isdigit()]
    if len(digitos) < 2:
        return False
    soma = 0
    for i, d in enumerate(reversed(digitos)):
        if i % 2 == 1:
            d *= 2
            if d > 9:
                d -= 9
        soma += d
    return soma % 10 == 0

for n in ["4111 1111 1111 1111", "4111 1111 1111 1112", "79927398713"]:
    print(n, luhn_valido(n))
