# Capítulo 6 — Listas e tuplos
# Secção: Ordenar

alunos = [("Rita", 16, 20), ("Hugo", 18, 19),
          ("Inês", 16, 18), ("Luís", 12, 21)]
# por nota decrescente e, em caso de empate, por nome
for nome, nota, idade in sorted(alunos, key=lambda a: (-a[1], a[0])):
    print(nome, nota, idade)
