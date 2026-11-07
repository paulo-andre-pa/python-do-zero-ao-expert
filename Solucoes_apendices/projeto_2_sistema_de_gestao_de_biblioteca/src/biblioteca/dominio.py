"""Entidades da biblioteca."""
from dataclasses import dataclass, field
from datetime import date, timedelta
from enum import Enum

MULTA_DIARIA = 0.50
MULTA_MAXIMA = 15.00

class TipoSocio(Enum):
    ESTUDANTE = (3, 14)
    DOCENTE = (8, 30)
    EXTERNO = (2, 7)

    def __init__(self, max_livros: int, dias: int) -> None:
        self.max_livros = max_livros
        self.dias = dias

@dataclass
class Livro:
    isbn: str
    titulo: str
    autor: str
    ano: int
    exemplares: int = 1

    def __post_init__(self) -> None:
        if self.exemplares < 1:
            raise ValueError("um livro tem pelo menos um exemplar")

@dataclass
class Socio:
    numero: int
    nome: str
    tipo: TipoSocio = TipoSocio.ESTUDANTE
    multas: float = 0.0

@dataclass
class Emprestimo:
    isbn: str
    socio: int
    saida: date
    prevista: date
    devolucao: date | None = None

    @classmethod
    def novo(cls, isbn: str, socio: Socio, hoje: date) -> "Emprestimo":
        return cls(isbn, socio.numero, hoje,
                   hoje + timedelta(days=socio.tipo.dias))

    @property
    def ativo(self) -> bool:
        return self.devolucao is None

    def dias_atraso(self, hoje: date) -> int:
        fim = self.devolucao or hoje
        return max(0, (fim - self.prevista).days)

    def multa(self, hoje: date) -> float:
        return min(MULTA_MAXIMA, self.dias_atraso(hoje) * MULTA_DIARIA)
