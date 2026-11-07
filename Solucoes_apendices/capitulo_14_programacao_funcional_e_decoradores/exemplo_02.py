# Capítulo 14 — Programação funcional e decoradores
# Secção: Funções lambda

from operator import itemgetter, attrgetter, mul

print(sorted(produtos, key=itemgetter(2), reverse=True)[0])
print(sorted(produtos, key=itemgetter(1, 0))[:2])

from dataclasses import dataclass
@dataclass
class Aluno:
    nome: str
    nota: float

turma = [Aluno("Rita", 15), Aluno("Hugo", 18), Aluno("Lia", 12)]
print(max(turma, key=attrgetter("nota")).nome, mul(6, 7))
