from ..produtos import Produto     # importação relativa

def pagar(produto: Produto, telemovel: str) -> str:
    return f"MB WAY: {produto.preco:.2f} € pedido a {telemovel}"
