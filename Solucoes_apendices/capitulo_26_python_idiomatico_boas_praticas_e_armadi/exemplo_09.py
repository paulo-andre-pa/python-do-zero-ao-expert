# Capítulo 26 — Python idiomático: boas práticas e armadilhas
# Secção: Funções

def classificar(idade):
    if idade < 0:
        raise ValueError("idade negativa")
    if idade < 18:
        return "menor"
    if idade < 65:
        return "adulto"
    return "sénior"

print([classificar(i) for i in (10, 30, 70)])
