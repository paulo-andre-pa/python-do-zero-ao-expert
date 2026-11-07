# Capítulo 20 — Concorrência: threads, processos e asyncio
# Secção: asyncio: concorrência com uma só thread

import asyncio

async def produtor(fila, n):
    for i in range(1, n + 1):
        await fila.put(f"pedido-{i}")
        await asyncio.sleep(0.005)

async def consumidor(nome, fila, feitos):
    while True:
        pedido = await fila.get()
        await asyncio.sleep(0.01)            # processa
        feitos.append((nome, pedido))
        fila.task_done()

async def main():
    fila: asyncio.Queue[str] = asyncio.Queue(maxsize=5)
    feitos: list[tuple[str, str]] = []
    consumidores = [asyncio.create_task(consumidor(f"C{i}", fila, feitos))
                    for i in range(3)]
    await produtor(fila, 10)
    await fila.join()                        # espera esvaziar
    for c in consumidores:
        c.cancel()
    print(len(feitos), "pedidos;", sorted({n for n, _ in feitos}))

asyncio.run(main())
