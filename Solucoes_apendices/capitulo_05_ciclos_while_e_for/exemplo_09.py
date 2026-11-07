# Capítulo 5 — Ciclos: while e for
# Secção: Controlar o ciclo: break, continue e else

for n in range(1, 11):
    if n % 3 == 0:
        continue          # ignora múltiplos de 3
    if n > 8:
        break             # pára aos 8
    print(n, end=" ")
print()
