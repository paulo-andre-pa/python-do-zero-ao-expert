# Capítulo 27 — Padrões de projeto e arquitetura
# Secção: Observer: reagir a eventos

from collections import defaultdict
from collections.abc import Callable

class BarramentoEventos:
    def __init__(self):
        self._subscritores: dict[str, list[Callable]] = defaultdict(list)

    def subscrever(self, evento: str):
        def registar(funcao):
            self._subscritores[evento].append(funcao)
            return funcao
        return registar

    def publicar(self, evento: str, **dados) -> None:
        for funcao in self._subscritores[evento]:
            funcao(**dados)

eventos = BarramentoEventos()

@eventos.subscrever("encomenda_paga")
def enviar_recibo(numero, cliente, total):
    print(f"e-mail para {cliente}: recibo da encomenda {numero}")

@eventos.subscrever("encomenda_paga")
def atualizar_stock(numero, **_):
    print(f"stock atualizado para a encomenda {numero}")

@eventos.subscrever("encomenda_paga")
def registar_contabilidade(numero, total, **_):
    print(f"lançamento contabilístico: {total:.2f} €")

eventos.publicar("encomenda_paga", numero=1042, cliente="sofia@ex.pt",
                 total=89.90)
