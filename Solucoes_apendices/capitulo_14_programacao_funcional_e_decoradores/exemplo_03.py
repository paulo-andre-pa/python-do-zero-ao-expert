# Capítulo 14 — Programação funcional e decoradores
# Secção: map, filter e reduce

precos = ["12.50", "3.20", "invalido", "47.00"]

def e_numero(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

validos = list(map(float, filter(e_numero, precos)))
print(validos)
print([float(p) for p in precos if e_numero(p)])   # equivalente
