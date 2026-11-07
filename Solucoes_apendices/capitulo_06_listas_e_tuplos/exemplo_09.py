# Capítulo 6 — Listas e tuplos
# Secção: Referências e cópias

a = [1, 2, 3]
c = a.copy()     # ou list(a) ou a[:]
c.append(4)
print(a, c, a is c)
