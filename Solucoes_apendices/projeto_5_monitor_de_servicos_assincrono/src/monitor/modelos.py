"""Resultados, estados e estatísticas de cada serviço."""
import statistics
from collections import deque
from dataclasses import dataclass, field
from enum import StrEnum

@dataclass(frozen=True)
class Resultado:
    ok: bool
    latencia_ms: float
    detalhe: str = ""

class Estado(StrEnum):
    DESCONHECIDO = "desconhecido"
    OPERACIONAL = "operacional"
    EM_FALHA = "em falha"

@dataclass(frozen=True)
class Alerta:
    servico: str
    anterior: Estado
    novo: Estado
    detalhe: str

@dataclass
class EstadoServico:
    nome: str
    limite_falhas: int = 3
    estado: Estado = Estado.DESCONHECIDO
    falhas_seguidas: int = 0
    historico: deque[Resultado] = field(
        default_factory=lambda: deque(maxlen=100))

    def registar(self, r: Resultado) -> Alerta | None:
        self.historico.append(r)
        anterior = self.estado
        if r.ok:
            self.falhas_seguidas = 0
            self.estado = Estado.OPERACIONAL
        else:
            self.falhas_seguidas += 1
            if self.falhas_seguidas >= self.limite_falhas:
                self.estado = Estado.EM_FALHA
        if self.estado != anterior and not (
                anterior is Estado.DESCONHECIDO
                and self.estado is Estado.OPERACIONAL):
            return Alerta(self.nome, anterior, self.estado, r.detalhe)
        return None

    @property
    def disponibilidade(self) -> float:
        if not self.historico:
            return 0.0
        return sum(r.ok for r in self.historico) / len(self.historico)

    def latencias(self) -> tuple[float, float]:
        valores = [r.latencia_ms for r in self.historico if r.ok]
        if len(valores) < 2:
            m = valores[0] if valores else 0.0
            return m, m
        p95 = statistics.quantiles(valores, n=20)[-1]
        return statistics.fmean(valores), p95
