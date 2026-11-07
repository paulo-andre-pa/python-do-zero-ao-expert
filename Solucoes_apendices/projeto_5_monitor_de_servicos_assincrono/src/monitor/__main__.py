"""Uso: python -m monitor monitor.toml [intervalo_em_segundos]"""
import asyncio
import sys
from pathlib import Path

from monitor.config import carregar
from monitor.notificadores import NotificadorConsola, NotificadorFicheiro
from monitor.nucleo import Monitor

def main() -> None:
    servicos = carregar(Path(sys.argv[1]))
    intervalo = float(sys.argv[2]) if len(sys.argv) > 2 else 30.0
    destinos = [NotificadorConsola(),
                NotificadorFicheiro(Path("alertas.jsonl"))]
    monitor = Monitor(servicos, destinos)
    try:
        asyncio.run(monitor.executar(intervalo))
    except KeyboardInterrupt:
        print("\n" + monitor.resumo())

if __name__ == "__main__":
    main()
