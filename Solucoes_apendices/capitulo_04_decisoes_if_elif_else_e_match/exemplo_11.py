# Capítulo 4 — Decisões: if, elif, else e match
# Secção: Planear decisões

def imposto(rendimento):
    total = 0.0
    if rendimento > 50_000:
        total += (rendimento - 50_000) * 0.40
        rendimento = 50_000
    if rendimento > 20_000:
        total += (rendimento - 20_000) * 0.28
        rendimento = 20_000
    if rendimento > 8_000:
        total += (rendimento - 8_000) * 0.15
    return total

for r in (5_000, 15_000, 35_000, 80_000):
    i = imposto(r)
    print(f"{r:>8,} € -> imposto {i:>10,.2f} € (taxa efetiva {i / r:.1%})")
