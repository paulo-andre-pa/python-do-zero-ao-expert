# Capítulo 20 — Concorrência: threads, processos e asyncio
# Secção: Threads com concurrent.futures

import random, time
from concurrent.futures import ThreadPoolExecutor, as_completed

def verificar_servico(nome):
    time.sleep(random.uniform(0.05, 0.2))
    if nome == "pagamentos":
        raise ConnectionError("timeout")
    return f"{nome} OK"

servicos = ["web", "api", "pagamentos", "email"]
with ThreadPoolExecutor() as ex:
    futuros = {ex.submit(verificar_servico, s): s for s in servicos}
    for fut in as_completed(futuros):
        try:
            print(fut.result())
        except ConnectionError as e:
            print(f"{futuros[fut]} FALHOU: {e}")
