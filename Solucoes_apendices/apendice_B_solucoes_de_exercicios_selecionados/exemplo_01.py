# Apêndice B — Soluções de exercícios selecionados
# Secção: Capítulo 2 — Variáveis, tipos e operadores

def formatar_duracao(total: int) -> str:
    horas, resto = divmod(total, 3600)
    minutos, segundos = divmod(resto, 60)
    return f"{horas:02d}:{minutos:02d}:{segundos:02d}"

for s in (0, 59, 3600, 7384, 86399):
    print(s, "->", formatar_duracao(s))
