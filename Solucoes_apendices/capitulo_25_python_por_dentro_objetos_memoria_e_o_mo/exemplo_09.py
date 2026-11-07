# Capítulo 25 — Python por dentro: objetos, memória e o modelo de dados
# Secção: Gestão de memória

import weakref

class Imagem:
    def __init__(self, nome):
        self.nome = nome

cache = weakref.WeakValueDictionary()
img = Imagem("logo.png")
cache["logo"] = img
print("logo" in cache)
del img                      # a única referência forte desaparece
print("logo" in cache)
