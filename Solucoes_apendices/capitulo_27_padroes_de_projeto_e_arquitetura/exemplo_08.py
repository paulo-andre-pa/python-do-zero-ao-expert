# Capítulo 27 — Padrões de projeto e arquitetura
# Secção: Injeção de dependências sem frameworks

from dataclasses import dataclass
from datetime import date
from typing import Protocol

class Relogio(Protocol):
    def hoje(self) -> date: ...

class Notificador(Protocol):
    def enviar(self, destino: str, texto: str) -> None: ...

@dataclass
class ServicoLembretes:          # domínio + aplicação: só conhece portas
    relogio: Relogio
    notificador: Notificador

    def lembrar_vencimentos(self, faturas: list[dict]) -> int:
        hoje = self.relogio.hoje()
        vencidas = [f for f in faturas
                    if f["vence"] < hoje and not f["paga"]]
        for f in vencidas:
            dias = (hoje - f["vence"]).days
            texto = f"Fatura {f['n']} vencida há {dias} dias"
            self.notificador.enviar(f["email"], texto)
        return len(vencidas)

class RelogioFixo:               # adaptadores (teste/demonstração)
    def __init__(self, d): self.d = d
    def hoje(self): return self.d

class NotificadorConsola:
    def enviar(self, destino, texto): print(f"-> {destino}: {texto}")

def main():                      # raiz de composição
    servico = ServicoLembretes(RelogioFixo(date(2026, 6, 15)),
                               NotificadorConsola())
    def fatura(n, email, vence, paga=False):
        return {"n": n, "email": email, "vence": vence, "paga": paga}
    faturas = [fatura("FT 31", "a@ex.pt", date(2026, 6, 1)),
               fatura("FT 32", "b@ex.pt", date(2026, 6, 30)),
               fatura("FT 33", "c@ex.pt", date(2026, 5, 2), paga=True)]
    print(servico.lembrar_vencimentos(faturas), "lembrete(s) enviado(s)")

main()
