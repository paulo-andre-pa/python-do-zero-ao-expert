"""Destinos dos alertas."""
import json
from datetime import datetime
from pathlib import Path
from typing import Protocol

from monitor.modelos import Alerta, Estado

class Notificador(Protocol):
    def notificar(self, alerta: Alerta) -> None: ...

class NotificadorConsola:
    def notificar(self, alerta: Alerta) -> None:
        icone = "[!]" if alerta.novo is Estado.EM_FALHA else "[ok]"
        print(f"{icone} {alerta.servico}: {alerta.anterior} -> "
              f"{alerta.novo} ({alerta.detalhe})")

class NotificadorFicheiro:
    """Grava um alerta por linha em formato JSON Lines."""
    def __init__(self, caminho: Path, relogio=datetime.now) -> None:
        self.caminho, self.relogio = caminho, relogio

    def notificar(self, alerta: Alerta) -> None:
        registo = {"quando": self.relogio().isoformat(timespec="seconds"),
                   "servico": alerta.servico, "estado": str(alerta.novo),
                   "detalhe": alerta.detalhe}
        with self.caminho.open("a", encoding="utf-8") as f:
            f.write(json.dumps(registo, ensure_ascii=False) + "\n")
