# Capítulo 9 — Ficheiros e exceções
# Secção: Escrever e ler

with open("notas.txt", encoding="utf-8") as f:
    for linha in f:
        nome, nota = linha.strip().split(";")
        print(f"{nome:<8} {int(nota):>3}")
