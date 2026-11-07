# Capítulo 7 — Dicionários e conjuntos
# Secção: Percorrer um dicionário

capitais = {"Portugal": "Lisboa", "Angola": "Luanda",
            "Brasil": "Brasília", "Moçambique": "Maputo"}

for pais in capitais:                     # percorre as chaves
    print(pais, end="; ")
print()
for pais, capital in capitais.items():    # pares chave-valor
    print(f"{pais:<12} -> {capital}")
print(list(capitais.values()))
