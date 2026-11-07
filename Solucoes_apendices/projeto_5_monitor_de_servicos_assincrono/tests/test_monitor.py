import asyncio
import json
import pytest
from monitor.config import ConfigServico, criar_verificador
from monitor.modelos import Estado, EstadoServico, Resultado
from monitor.notificadores import NotificadorFicheiro
from monitor.nucleo import Monitor

class VerificadorProgramado:
    def __init__(self, sequencia: str, atraso: float = 0.0):
        self.sequencia = iter(sequencia)   # p. ex. "oo-x--o"
        self.atraso = atraso
    async def verificar(self):
        await asyncio.sleep(self.atraso)
        ok = next(self.sequencia) == "o"
        return Resultado(ok, 10.0, "ok" if ok else "falha")

class Memoria:
    def __init__(self):
        self.alertas = []
    def notificar(self, alerta):
        self.alertas.append(alerta)

def correr(sequencia, rondas, limite=3, **kw):
    destino = Memoria()
    cfg = ConfigServico("api", VerificadorProgramado(sequencia, **kw),
                        timeout=0.05, limite_falhas=limite)
    m = Monitor([cfg], [destino])
    for _ in range(rondas):
        asyncio.run(m.ronda())
    return m, [(a.anterior, a.novo) for a in destino.alertas]

def test_falha_isolada_nao_gera_alerta():
    _, alertas = correr("oo-oo-o", 7)
    assert alertas == []

def test_alerta_apos_tres_falhas_e_recuperacao():
    m, alertas = correr("o---oo", 6)
    assert alertas == [(Estado.OPERACIONAL, Estado.EM_FALHA),
                       (Estado.EM_FALHA, Estado.OPERACIONAL)]
    assert m.estados["api"].disponibilidade == pytest.approx(3 / 6)

def test_timeout_conta_como_falha():
    m, alertas = correr("ooo", 1, limite=1, atraso=0.2)
    assert m.estados["api"].estado is Estado.EM_FALHA

def test_estatisticas_latencia():
    e = EstadoServico("x")
    for ms in [10, 20, 30, 40, 1000]:
        e.registar(Resultado(True, ms))
    media, p95 = e.latencias()
    assert media == 220 and p95 > 40

def test_configuracao_invalida():
    with pytest.raises(ValueError):
        criar_verificador({"tipo": "tcp", "host": "x"})   # sem porta

def test_notificador_ficheiro(tmp_path):
    from datetime import datetime
    from monitor.modelos import Alerta
    f = tmp_path / "a.jsonl"
    n = NotificadorFicheiro(f, relogio=lambda: datetime(2026, 1, 1, 9))
    n.notificar(Alerta("db", Estado.OPERACIONAL, Estado.EM_FALHA, "t/o"))
    assert json.loads(f.read_text())["estado"] == "em falha"
