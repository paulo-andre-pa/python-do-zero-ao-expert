# Capítulo 20 — Concorrência: threads, processos e asyncio
# Secção: Qual escolher?

import asyncio, random
from collections import Counter

async def verificar(url: str) -> int:
    await asyncio.sleep(random.uniform(0.005, 0.15))
    return random.choices([200, 301, 404], weights=[85, 10, 5])[0]

async def verificar_com_limites(url, semaforo):
    async with semaforo:
        try:
            async with asyncio.timeout(0.1):
                return url, await verificar(url)
        except TimeoutError:
            return url, "timeout"

async def auditar(urls):
    semaforo = asyncio.Semaphore(8)
    async with asyncio.TaskGroup() as tg:
        tarefas = [tg.create_task(verificar_com_limites(u, semaforo))
                   for u in urls]
    return [t.result() for t in tarefas]

urls = [f"/pagina/{i}" for i in range(40)]
resultados = asyncio.run(auditar(urls))
print(Counter(estado for _, estado in resultados))
problemas = [u for u, e in resultados if e in (404, "timeout")]
print(len(problemas), "com problemas, p. ex.:", problemas[:4])
