"""Modelos de domínio do gestor de tarefas."""
from dataclasses import dataclass, field
from datetime import date
from enum import IntEnum

class Prioridade(IntEnum):
    ALTA = 1
    MEDIA = 2
    BAIXA = 3

    @classmethod
    def de_texto(cls, texto: str) -> "Prioridade":
        normal = texto.strip().upper().replace("É", "E")
        try:
            return cls[normal]
        except KeyError:
            opcoes = ", ".join(p.name.lower() for p in cls)
            raise ValueError(
                f"prioridade inválida: '{texto}' (use {opcoes})") from None

@dataclass
class Tarefa:
    titulo: str
    prioridade: Prioridade = Prioridade.MEDIA
    prazo: date | None = None
    etiquetas: list[str] = field(default_factory=list)
    concluida: bool = False
    id: int | None = None

    def __post_init__(self) -> None:
        self.titulo = self.titulo.strip()
        if not self.titulo:
            raise ValueError("o título não pode estar vazio")
        if len(self.titulo) > 120:
            raise ValueError("o título não pode exceder 120 carateres")
        self.etiquetas = sorted({e.strip().lower()
                                 for e in self.etiquetas if e.strip()})

    def atrasada(self, hoje: date) -> bool:
        return (not self.concluida and self.prazo is not None
                and self.prazo < hoje)
