# Capítulo 12 — POO avançada: herança, dataclasses e métodos especiais
# Secção: Dataclasses

from dataclasses import dataclass, field
from datetime import date

@dataclass
class Tarefa:
    titulo: str
    prioridade: int = 3
    concluida: bool = False
    etiquetas: list[str] = field(default_factory=list)
    criada: date = field(default_factory=lambda: date(2026, 1, 15))

    def concluir(self):
        self.concluida = True

t = Tarefa("Preparar apresentação", prioridade=1, etiquetas=["trabalho"])
print(t)
t.concluir()
print(t.concluida, t == Tarefa("Preparar apresentação", 1))
