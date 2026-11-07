# Capítulo 20 — Concorrência: threads, processos e asyncio
# Secção: Partilhar dados: condições de corrida

import threading

class ContaPartilhada:
    def __init__(self):
        self.saldo = 0
        self._lock = threading.Lock()

    def depositar(self, valor, vezes):
        for _ in range(vezes):
            with self._lock:             # secção crítica
                atual = self.saldo
                self.saldo = atual + valor

conta = ContaPartilhada()
threads = [threading.Thread(target=conta.depositar, args=(1, 50_000))
           for _ in range(4)]
for t in threads:
    t.start()
for t in threads:
    t.join()                             # espera que terminem
print("saldo final:", conta.saldo)       # sempre 200000
