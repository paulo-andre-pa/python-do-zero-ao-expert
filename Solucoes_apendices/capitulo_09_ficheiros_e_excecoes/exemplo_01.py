# Capítulo 9 — Ficheiros e exceções
# Secção: Escrever e ler

with open("notas.txt", "w", encoding="utf-8") as f:
    f.write("Ana;17\n")
    f.write("Bruno;13\n")
    f.writelines(["Carla;19\n", "Duarte;11\n"])

with open("notas.txt", encoding="utf-8") as f:
    conteudo = f.read()
print(conteudo)
