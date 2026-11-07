# Capítulo 20 — Concorrência: threads, processos e asyncio
# Secção: Threads com concurrent.futures

import time
from concurrent.futures import ThreadPoolExecutor

def descarregar(url):
    time.sleep(0.2)                      # simula a espera pela rede
    return f"{url}: {len(url) * 100} bytes"

urls = [f"https://exemplo.pt/pagina{i}" for i in range(10)]

inicio = time.perf_counter()
resultados = [descarregar(u) for u in urls]
sequencial = time.perf_counter() - inicio

inicio = time.perf_counter()
with ThreadPoolExecutor(max_workers=10) as executor:
    resultados = list(executor.map(descarregar, urls))
concorrente = time.perf_counter() - inicio

print(resultados[0])
print(f"sequencial ~{sequencial:.1f}s | com threads ~{concorrente:.1f}s")
