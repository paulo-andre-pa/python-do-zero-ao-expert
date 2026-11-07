from dataclasses import dataclass

@dataclass
class Linha:
    produto: str
    quantidade: int
    preco: float

def total(linhas: list[Linha]) -> float:
    return sum(l.quantidade * l.preco for l in linhas)

def procurar(linhas: list[Linha], produto: str) -> Linha | None:
    for l in linhas:
        if l.produto == produto:
            return l
    return None

def desconto_do_produto(linhas: list[Linha], produto: str) -> float:
    linha = procurar(linhas, produto)
    return linha.preco * 0.1

def relatorio(linhas: list[Linha]) -> str:
    return "Total: " + total(linhas)

encomenda = [Linha("Caneta", "3", 1.2)]
