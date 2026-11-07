# Capítulo 20 — Concorrência: threads, processos e asyncio
# Secção: asyncio: concorrência com uma só thread

import asyncio, time

async def preparar(prato, minutos):
    print(f"início: {prato}")
    await asyncio.sleep(minutos / 10)    # espera sem bloquear
    print(f"pronto: {prato}")
    return prato

async def jantar():
    inicio = time.perf_counter()
    pratos = await asyncio.gather(
        preparar("sopa", 3),
        preparar("arroz", 2),
        preparar("salada", 1),
    )
    print(pratos, f"em ~{time.perf_counter() - inicio:.1f}s")

asyncio.run(jantar())
