# Capítulo 6 — Listas e tuplos
# Secção: Referências e cópias

a = [1, 2, 3]
b = a            # b e a são o MESMO objeto
b.append(4)
print(a, b, a is b)
