# Capítulo 25 — Python por dentro: objetos, memória e o modelo de dados
# Secção: Gestão de memória

import gc

class No:
    def __init__(self, nome):
        self.nome, self.vizinho = nome, None
    def __del__(self):
        print(f"[nó {self.nome} libertado]")

a, b = No("A"), No("B")
a.vizinho, b.vizinho = b, a      # ciclo A <-> B
del a, b
print("sem nomes, mas o ciclo mantém as referências")
print("objetos recolhidos:", gc.collect() >= 2)
