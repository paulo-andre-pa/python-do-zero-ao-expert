# Capítulo 5 — Ciclos: while e for
# Secção: Ciclos aninhados

for linha in range(1, 5):
    for coluna in range(1, 5):
        print(f"{linha * coluna:4}", end="")
    print()
