# Capítulo 20 — Concorrência: threads, processos e asyncio
# Secção: asyncio: concorrência com uma só thread

import asyncio, random

async def consultar_api(cliente_id, limite):
    async with limite:                       # no máximo 3 de cada vez
        await asyncio.sleep(random.uniform(0.01, 0.05))
        return {"id": cliente_id, "saldo": cliente_id * 10}

async def com_timeout(segundos):
    try:
        async with asyncio.timeout(segundos):
            await asyncio.sleep(1)           # operação demasiado lenta
    except TimeoutError:
        return f"cancelado após {segundos}s"

async def principal():
    limite = asyncio.Semaphore(3)
    async with asyncio.TaskGroup() as tg:
        tarefas = [tg.create_task(consultar_api(i, limite))
                   for i in range(1, 9)]
    saldos = [t.result()["saldo"] for t in tarefas]
    print("saldos:", saldos)
    print(await com_timeout(0.1))

asyncio.run(principal())
