# Capítulo 11 — Programação orientada a objetos
# Secção: Representação de objetos

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __repr__(self):
        return f"Produto({self.nome!r}, {self.preco!r})"

    def __str__(self):
        return f"{self.nome} — {self.preco:.2f} €"

p = Produto("Auscultadores", 59.9)
print(p)            # usa __str__
print(repr(p))      # usa __repr__
print([p])          # dentro de listas, usa __repr__
