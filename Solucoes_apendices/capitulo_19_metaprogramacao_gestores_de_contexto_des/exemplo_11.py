# Capítulo 19 — Metaprogramação: gestores de contexto, descritores e metaclasses
# Secção: Personalizar a criação de classes

class MetaDocumentada(type):
    classes: list[str] = []

    def __new__(mcs, nome, bases, atributos):
        if not atributos.get("__doc__"):
            raise TypeError(f"A classe {nome} precisa de docstring")
        cls = super().__new__(mcs, nome, bases, atributos)
        mcs.classes.append(nome)
        return cls

class Servico(metaclass=MetaDocumentada):
    """Classe base de todos os serviços."""

class ServicoEmail(Servico):
    """Envia e-mails transacionais."""

try:
    class ServicoSemDoc(Servico):
        pass
except TypeError as e:
    print(e)
print(MetaDocumentada.classes)
