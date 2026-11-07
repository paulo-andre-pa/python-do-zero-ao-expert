# Capítulo 27 — Padrões de projeto e arquitetura
# Secção: Factory: centralizar a criação de objetos

from typing import Protocol

class Exportador(Protocol):
    def exportar(self, linhas: list[dict]) -> str: ...

class CSV:
    def exportar(self, linhas):
        cab = ";".join(linhas[0])
        corpo = [";".join(map(str, l.values())) for l in linhas]
        return "\n".join([cab, *corpo])

class Markdown:
    def exportar(self, linhas):
        cab = "| " + " | ".join(linhas[0]) + " |"
        sep = "|" + "---|" * len(linhas[0])
        corpo = ["| " + " | ".join(map(str, l.values())) + " |"
                 for l in linhas]
        return "\n".join([cab, sep, *corpo])

_REGISTO: dict[str, type] = {"csv": CSV, "md": Markdown}

def criar_exportador(formato: str) -> Exportador:
    try:
        return _REGISTO[formato.lower()]()
    except KeyError:
        raise ValueError(f"formato desconhecido: {formato}") from None

dados = [{"produto": "Café", "qtd": 3}, {"produto": "Chá", "qtd": 1}]
print(criar_exportador("md").exportar(dados))
