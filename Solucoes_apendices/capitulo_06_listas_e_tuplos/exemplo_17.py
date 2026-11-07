# Capítulo 6 — Listas e tuplos
# Secção: Listas de listas: dados tabulares

ESCALOES = [(50_000, 0.40), (20_000, 0.28), (8_000, 0.15), (0, 0.0)]

def imposto(rendimento):
    total = 0.0
    for limite, taxa in ESCALOES:
        if rendimento > limite:
            total += (rendimento - limite) * taxa
            rendimento = limite
    return total

for r in (5_000, 15_000, 35_000, 80_000):
    print(f"{r:>7,} € -> {imposto(r):>9,.2f} €")
