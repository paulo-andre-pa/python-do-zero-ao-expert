# Capítulo 6 — Listas e tuplos
# Secção: Compreensões de lista: uma primeira visita

numeros = range(1, 11)

quadrados = []
for n in numeros:
    quadrados.append(n ** 2)

quadrados2 = [n ** 2 for n in numeros]
pares = [n for n in numeros if n % 2 == 0]
print(quadrados == quadrados2, pares)
