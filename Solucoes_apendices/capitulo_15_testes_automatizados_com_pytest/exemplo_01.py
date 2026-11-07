# Capítulo 15 — Testes automatizados com pytest
# Secção: A instrução assert

def media(valores):
    return sum(valores) / len(valores)

assert media([10, 20]) == 15
assert media([7]) == 7
print("Todos os testes passaram")
