# Capítulo 6 — Listas e tuplos
# Secção: Tuplos: sequências imutáveis

def estatisticas(valores):
    return min(valores), max(valores), sum(valores) / len(valores)

minimo, maximo, media = estatisticas([4, 8, 15, 16, 23, 42])
print(minimo, maximo, round(media, 2))
