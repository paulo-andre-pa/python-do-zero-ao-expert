# Capítulo 5 — Ciclos: while e for
# Secção: O ciclo while

# Quantos anos até duplicar um capital a 4 % ao ano?
capital = 1000.0
anos = 0
while capital < 2000:
    capital *= 1.04
    anos += 1
print(f"{anos} anos (capital final: {capital:.2f} €)")
