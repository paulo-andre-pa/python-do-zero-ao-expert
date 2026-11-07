# Capítulo 25 — Python por dentro: objetos, memória e o modelo de dados
# Secção: Memória das estruturas de dados

import sys

lista = []
anterior = sys.getsizeof(lista)
print(f"vazia: {anterior} bytes")
for i in range(20):
    lista.append(i)
    tamanho = sys.getsizeof(lista)
    if tamanho != anterior:
        print(f"com {len(lista):>2} elementos: {tamanho} bytes")
        anterior = tamanho
