# Capítulo 11 — Programação orientada a objetos
# Secção: Pensar em objetos: da descrição às classes

class Carrinho:
    PORTES = 4.99
    LIMITE_PORTES_GRATIS = 50
    CUPOES = {"DESC10": 0.10}

    def __init__(self):
        self._itens = {}        # nome -> [preco, qtd]
        self._desconto = 0.0

    def adicionar(self, nome, preco, qtd=1):
        if preco < 0 or qtd < 1:
            raise ValueError("Preço ou quantidade inválidos")
        if nome in self._itens:
            self._itens[nome][1] += qtd
        else:
            self._itens[nome] = [preco, qtd]

    def remover(self, nome):
        if nome not in self._itens:
            raise KeyError(f"'{nome}' não está no carrinho")
        del self._itens[nome]

    def aplicar_cupao(self, codigo):
        if self._desconto:
            raise ValueError("Já foi aplicado um cupão")
        self._desconto = self.CUPOES[codigo]

    @property
    def subtotal(self):
        bruto = sum(p * q for p, q in self._itens.values())
        return round(bruto * (1 - self._desconto), 2)

    @property
    def portes(self):
        if not self._itens or self.subtotal >= self.LIMITE_PORTES_GRATIS:
            return 0.0
        return self.PORTES

    @property
    def total(self):
        return round(self.subtotal + self.portes, 2)

    def __len__(self):
        return sum(q for _, q in self._itens.values())

    def __repr__(self):
        return f"Carrinho({len(self)} artigos, total={self.total} €)"

c = Carrinho()
c.adicionar("T-shirt", 14.90, 2)
c.adicionar("Boné", 12.00)
print(c, "| portes:", c.portes)
c.adicionar("Boné", 12.00)
c.aplicar_cupao("DESC10")
print(c, "| portes:", c.portes)
