# Capítulo 19 — Metaprogramação: gestores de contexto, descritores e metaclasses
# Secção: Controlar o acesso a atributos

class Auditado:
    def __init__(self, **campos):
        super().__setattr__("historico", [])
        for k, v in campos.items():
            setattr(self, k, v)

    def __setattr__(self, nome, valor):
        antigo = getattr(self, nome, None)
        self.historico.append((nome, antigo, valor))
        super().__setattr__(nome, valor)

e = Auditado(estado="rascunho")
e.estado = "aprovado"
print(e.historico)
