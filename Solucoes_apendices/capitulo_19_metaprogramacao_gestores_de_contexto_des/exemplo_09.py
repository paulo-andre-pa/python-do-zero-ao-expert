# Capítulo 19 — Metaprogramação: gestores de contexto, descritores e metaclasses
# Secção: Personalizar a criação de classes

class Exportador:
    registo: dict[str, type] = {}

    def __init_subclass__(cls, formato: str, **kwargs):
        super().__init_subclass__(**kwargs)
        Exportador.registo[formato] = cls

    def exportar(self, dados): ...

class ExportadorCSV(Exportador, formato="csv"):
    def exportar(self, dados):
        return "\n".join(";".join(map(str, l)) for l in dados)

class ExportadorMarkdown(Exportador, formato="md"):
    def exportar(self, dados):
        linhas = ("| " + " | ".join(map(str, l)) + " |" for l in dados)
        return "\n".join(linhas)

def exportar(dados, formato):
    return Exportador.registo[formato]().exportar(dados)

tabela = [("Produto", "Qtd"), ("Café", 3)]
print(sorted(Exportador.registo))
print(exportar(tabela, "md"))
