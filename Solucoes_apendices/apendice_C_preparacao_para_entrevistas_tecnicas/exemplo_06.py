# Apêndice C — Preparação para entrevistas técnicas
# Secção: Exercícios típicos (com soluções)

from collections import OrderedDict

class CacheLRU:
    def __init__(self, capacidade: int):
        self.capacidade = capacidade
        self._dados: OrderedDict = OrderedDict()

    def get(self, chave):
        if chave not in self._dados:
            return None
        self._dados.move_to_end(chave)          # usado agora
        return self._dados[chave]

    def put(self, chave, valor) -> None:
        self._dados[chave] = valor
        self._dados.move_to_end(chave)
        if len(self._dados) > self.capacidade:
            self._dados.popitem(last=False)     # remove o mais antigo

c = CacheLRU(2)
c.put("a", 1); c.put("b", 2); c.get("a"); c.put("c", 3)
print(list(c._dados), c.get("b"))
