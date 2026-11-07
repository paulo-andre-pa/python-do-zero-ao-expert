# Capítulo 12 — POO avançada: herança, dataclasses e métodos especiais
# Secção: Dataclasses

@dataclass
class Aluno:
    numero: int
    nome: str
    nota: float

    def __post_init__(self):
        if not 0 <= self.nota <= 20:
            raise ValueError(f"Nota inválida para {self.nome}: {self.nota}")
        self.nome = self.nome.strip().title()

print(Aluno(2026001, "  joana reis ", 17.5))
