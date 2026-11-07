# Capítulo 25 — Python por dentro: objetos, memória e o modelo de dados
# Secção: Âmbitos e *closures* por dentro

import gc, weakref

class Janela:
    vivas = 0
    def __init__(self):
        Janela.vivas += 1
    def __del__(self):
        Janela.vivas -= 1
    def ao_evento(self, e):
        pass

class EmissorForte:
    def __init__(self):
        self.ouvintes = []
    def subscrever(self, f):
        self.ouvintes.append(f)

class EmissorFraco:
    def __init__(self):
        self.ouvintes = []
    def subscrever(self, metodo):
        self.ouvintes.append(weakref.WeakMethod(metodo))
    def emitir(self, evento):
        vivos = [ref for ref in self.ouvintes if ref() is not None]
        for ref in vivos:
            ref()(evento)
        self.ouvintes = vivos          # limpa as referências mortas

for Emissor in (EmissorForte, EmissorFraco):
    emissor = Emissor()
    janelas = [Janela() for _ in range(1000)]
    for j in janelas:
        emissor.subscrever(j.ao_evento)
    del janelas, j
    gc.collect()
    print(f"{Emissor.__name__}: {Janela.vivas} janelas ainda em memória")
    del emissor
    gc.collect()
