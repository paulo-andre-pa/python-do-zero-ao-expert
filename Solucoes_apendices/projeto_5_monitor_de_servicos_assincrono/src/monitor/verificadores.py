"""Verificadores assíncronos: HTTP e TCP."""
import asyncio
import time
from typing import Protocol
from urllib.parse import urlsplit

from monitor.modelos import Resultado

class Verificador(Protocol):
    async def verificar(self) -> Resultado: ...

class VerificadorTCP:
    def __init__(self, host: str, porta: int) -> None:
        self.host, self.porta = host, porta

    async def verificar(self) -> Resultado:
        t0 = time.perf_counter()
        try:
            _, escritor = await asyncio.open_connection(self.host,
                                                        self.porta)
        except OSError as e:
            return Resultado(False, 0.0, f"ligação recusada ({e.errno})")
        escritor.close()
        await escritor.wait_closed()
        ms = (time.perf_counter() - t0) * 1000
        return Resultado(True, ms, "porta aberta")

class VerificadorHTTP:
    """Pedido HTTP/1.1 mínimo escrito diretamente sobre asyncio."""
    def __init__(self, url: str) -> None:
        partes = urlsplit(url)
        self.host = partes.hostname or "localhost"
        self.porta = partes.port or 80
        self.caminho = partes.path or "/"

    async def verificar(self) -> Resultado:
        t0 = time.perf_counter()
        try:
            leitor, escritor = await asyncio.open_connection(self.host,
                                                             self.porta)
            escritor.write(f"GET {self.caminho} HTTP/1.1\r\n"
                           f"Host: {self.host}\r\nConnection: close\r\n\r\n"
                           .encode())
            await escritor.drain()
            linha = (await leitor.readline()).decode(errors="replace")
            escritor.close()
            await escritor.wait_closed()
        except OSError as e:
            return Resultado(False, 0.0, f"erro de rede ({e.errno})")
        ms = (time.perf_counter() - t0) * 1000
        try:
            codigo = int(linha.split()[1])
        except (IndexError, ValueError):
            return Resultado(False, ms, "resposta HTTP inválida")
        return Resultado(200 <= codigo < 400, ms, f"HTTP {codigo}")
