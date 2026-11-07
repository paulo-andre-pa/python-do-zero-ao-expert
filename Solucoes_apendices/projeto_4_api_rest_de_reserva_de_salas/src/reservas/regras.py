"""Regras de negócio das reservas (sem HTTP nem SQL)."""
from dataclasses import dataclass
from datetime import datetime, time, timedelta

ABERTURA, FECHO = time(8, 0), time(20, 0)
DURACAO_MAXIMA = timedelta(hours=4)

class ReservaInvalida(ValueError):
    pass

class Conflito(Exception):
    pass

@dataclass(frozen=True)
class Intervalo:
    inicio: datetime
    fim: datetime

    def sobrepoe(self, outro: "Intervalo") -> bool:
        return self.inicio < outro.fim and outro.inicio < self.fim

def validar(intervalo: Intervalo, participantes: int,
            capacidade: int) -> None:
    i, f = intervalo.inicio, intervalo.fim
    if f <= i:
        raise ReservaInvalida("o fim tem de ser posterior ao início")
    if i.weekday() >= 5:
        raise ReservaInvalida("só são permitidas reservas em dias úteis")
    if i.date() != f.date() or i.time() < ABERTURA or f.time() > FECHO:
        raise ReservaInvalida("horário permitido: 08:00 às 20:00")
    if f - i > DURACAO_MAXIMA:
        raise ReservaInvalida("duração máxima: 4 horas")
    if not 1 <= participantes <= capacidade:
        raise ReservaInvalida(
            f"participantes devem estar entre 1 e {capacidade}")
