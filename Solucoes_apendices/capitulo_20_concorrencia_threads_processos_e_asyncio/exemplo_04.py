# Capítulo 20 — Concorrência: threads, processos e asyncio
# Secção: Partilhar dados: condições de corrida

import queue, threading, time

fila: queue.Queue = queue.Queue()
resultados = []
lock_resultados = threading.Lock()

def trabalhador(nome):
    while True:
        tarefa = fila.get()
        if tarefa is None:               # sinal de paragem
            fila.task_done()
            break
        time.sleep(0.01)                 # processa a tarefa
        with lock_resultados:
            resultados.append((tarefa, nome))
        fila.task_done()

trabalhadores = [threading.Thread(target=trabalhador, args=(f"T{i}",))
                 for i in range(3)]
for t in trabalhadores:
    t.start()
for encomenda in range(1, 13):
    fila.put(f"encomenda-{encomenda}")
for _ in trabalhadores:
    fila.put(None)
fila.join()
print(len(resultados), "encomendas processadas por",
      sorted({nome for _, nome in resultados}))
