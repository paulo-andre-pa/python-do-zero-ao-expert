# Apêndice B — Soluções de exercícios selecionados
# Secção: Capítulo 5 — Ciclos

primos = []
for n in range(2, 100):
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            break
    else:
        primos.append(n)
print(len(primos), primos)
