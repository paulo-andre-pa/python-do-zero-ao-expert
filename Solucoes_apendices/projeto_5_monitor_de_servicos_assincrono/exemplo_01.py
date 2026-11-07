# Projeto 5 — Monitor de serviços assíncrono
# Secção: Utilização

import asyncio, socket
from pathlib import Path
from monitor.config import carregar
from monitor.notificadores import NotificadorConsola
from monitor.nucleo import Monitor

def servidor_http(comportamento):
    pedidos = 0
    async def tratar(leitor, escritor):
        nonlocal pedidos
        pedidos += 1
        codigo, atraso = comportamento(pedidos)
        try:
            await leitor.readuntil(b"\r\n\r\n")
            await asyncio.sleep(atraso)
            escritor.write(f"HTTP/1.1 {codigo} X\r\n\r\n".encode())
            await escritor.drain()
        except (ConnectionError, asyncio.IncompleteReadError):
            pass                        # o cliente desistiu (timeout)
        finally:
            escritor.close()
    return tratar

def porta_livre():
    with socket.socket() as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]

async def demonstracao():
    portas = {}
    comportamentos = {
        "site": lambda n: (200, 0.0),
        "pagamentos": lambda n: (500 if 3 <= n <= 6 else 200, 0.0),
        "relatorios": lambda n: (200, 0.5),          # demasiado lento
    }
    servidores = []
    for nome, comp in comportamentos.items():
        srv = await asyncio.start_server(servidor_http(comp),
                                         "127.0.0.1", 0)
        servidores.append(srv)
        portas[nome] = srv.sockets[0].getsockname()[1]
    portas["email"] = porta_livre()                  # ninguém a escutar

    Path("monitor.toml").write_text(f"""
[omissoes]
timeout = 0.3
limite_falhas = 3

[[servico]]
nome = "site"
tipo = "http"
url = "http://127.0.0.1:{portas['site']}/"

[[servico]]
nome = "pagamentos"
tipo = "http"
url = "http://127.0.0.1:{portas['pagamentos']}/saude"

[[servico]]
nome = "relatorios"
tipo = "http"
url = "http://127.0.0.1:{portas['relatorios']}/"

[[servico]]
nome = "email"
tipo = "tcp"
host = "127.0.0.1"
porta = {portas['email']}
""", encoding="utf-8")

    servicos = carregar(Path("monitor.toml"))
    monitor = Monitor(servicos, [NotificadorConsola()])
    for ronda in range(1, 10):
        print(f"-- ronda {ronda}")
        await monitor.ronda()
    for srv in servidores:
        srv.close()
    return monitor

monitor = asyncio.run(demonstracao())
