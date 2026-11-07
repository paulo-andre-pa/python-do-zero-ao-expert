# Capítulo 25 — Python por dentro: objetos, memória e o modelo de dados
# Secção: Gestão de memória

import sys

class Recurso:
    def __init__(self, nome):
        self.nome = nome
    def __del__(self):
        print(f"[{self.nome} libertado]")

r = Recurso("ligação")
outra = r
print(sys.getrefcount(r) - 1)   # -1: o próprio argumento conta
del r
print("após del r: ainda existe uma referência")
outra = None
print("fim")
