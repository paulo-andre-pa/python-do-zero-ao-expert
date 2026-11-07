# Capítulo 5 — Ciclos: while e for
# Secção: O ciclo for

alunos = ["Ana", "Bruno", "Carla"]
notas = [16, 12, 18]
for aluno, nota in zip(alunos, notas):
    print(f"{aluno:<6} {nota}")
