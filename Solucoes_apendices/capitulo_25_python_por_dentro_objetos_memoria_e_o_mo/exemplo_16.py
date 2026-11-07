# Capítulo 25 — Python por dentro: objetos, memória e o modelo de dados
# Secção: Memória das estruturas de dados

import array, sys

numeros = list(range(10_000))
ints = sum(map(sys.getsizeof, numeros))      # os objetos int
print("list :", sys.getsizeof(numeros) + ints)
print("tuple:", sys.getsizeof(tuple(numeros)) + ints)
print("array:", sys.getsizeof(array.array("i", numeros)))
print("range:", sys.getsizeof(range(10_000)))
