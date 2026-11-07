"""Orquestração das verificações e dos alertas."""
import asyncio
from collections.abc import Sequence

from monitor.config import ConfigServico
from monitor.modelos import Alerta, EstadoServico, Resultado
from monitor.notificadores import Notificador

class Monitor:
    def __init__(self, servicos: Sequence[ConfigServico],
                 notificadores: Sequence[Notificador] = ()) -> None:
        self.servicos = list(servicos)
        self.notificadores = list(notificadores)
        self.estados = {s.nome: EstadoServico(s.nome, s.limite_falhas)
                        for s in self.servicos}

    async def _verificar(self, s: ConfigServico) -> Resultado:
        try:
            async with asyncio.timeout(s.timeout):
                return await s.verificador.verificar()
        except TimeoutError:
            return Resultado(False, s.timeout * 1000, "timeout")

    async def ronda(self) -> list[Alerta]:
        async with asyncio.TaskGroup() as tg:
            tarefas = {s.nome: tg.create_task(self._verificar(s))
                       for s in self.servicos}
        alertas = []
        for nome, tarefa in tarefas.items():
            alerta = self.estados[nome].registar(tarefa.result())
            if alerta:
                alertas.append(alerta)
                for n in self.notificadores:
                    n.notificar(alerta)
        return alertas

    async def executar(self, intervalo: float, rondas: int | None = None):
        feitas = 0
        while rondas is None or feitas < rondas:
            await self.ronda()
            feitas += 1
            await asyncio.sleep(intervalo)

    def resumo(self) -> str:
        linhas = [f"{'serviço':<14}{'estado':<14}{'disp.':>7}"
                  f"{'média':>9}{'p95':>9}"]
        for nome, e in self.estados.items():
            media, p95 = e.latencias()
            lat = (f"{media:>7.1f}ms{p95:>7.1f}ms" if e.disponibilidade
                   else f"{'—':>9}{'—':>9}")
            linhas.append(f"{nome:<14}{e.estado:<14}"
                          f"{e.disponibilidade:>7.0%}{lat}")
        return "\n".join(linhas)
