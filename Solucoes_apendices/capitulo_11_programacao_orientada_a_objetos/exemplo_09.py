# Capítulo 11 — Programação orientada a objetos
# Secção: Composição: objetos que contêm objetos

class Produto:
    def __init__(self, codigo, nome, preco):
        self.codigo, self.nome, self.preco = codigo, nome, preco

class LinhaEncomenda:
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade

    @property
    def subtotal(self):
        return self.produto.preco * self.quantidade

class Encomenda:
    def __init__(self, cliente):
        self.cliente = cliente
        self.linhas = []

    def adicionar(self, produto, quantidade=1):
        for linha in self.linhas:
            if linha.produto.codigo == produto.codigo:
                linha.quantidade += quantidade
                return
        self.linhas.append(LinhaEncomenda(produto, quantidade))

    @property
    def total(self):
        return sum(l.subtotal for l in self.linhas)

    def resumo(self):
        txt = [f"Encomenda de {self.cliente}"]
        for l in self.linhas:
            txt.append(f"  {l.quantidade} x {l.produto.nome:<14}"
                       f"{l.subtotal:>8.2f} €")
        txt.append(f"  {'TOTAL':<18}{self.total:>8.2f} €")
        return "\n".join(txt)

livro = Produto("L01", "Livro Python", 34.90)
caneca = Produto("C07", "Caneca", 8.50)
enc = Encomenda("Sofia")
enc.adicionar(livro)
enc.adicionar(caneca, 2)
enc.adicionar(caneca)
print(enc.resumo())
