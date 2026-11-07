# Capítulo 12 — POO avançada: herança, dataclasses e métodos especiais
# Secção: Herança múltipla e a MRO

import json

class JsonMixin:
    def para_json(self):
        return json.dumps(self.__dict__, ensure_ascii=False)

class ComparavelPorIdMixin:
    def __eq__(self, outro):
        return type(self) is type(outro) and self.id == outro.id

class Cliente(JsonMixin, ComparavelPorIdMixin):
    def __init__(self, id, nome):
        self.id, self.nome = id, nome

c1, c2 = Cliente(7, "Lúcia"), Cliente(7, "Lúcia M.")
print(c1.para_json(), c1 == c2)
print([k.__name__ for k in Cliente.__mro__])
