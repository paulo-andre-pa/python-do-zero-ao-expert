# Apêndice B — Soluções de exercícios selecionados
# Secção: Capítulo 4 — Decisões

def bissexto(ano: int) -> bool:
    return ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)

print({a: bissexto(a) for a in (1900, 2000, 2024, 2026)})
