# Capítulo 19 — Metaprogramação: gestores de contexto, descritores e metaclasses
# Secção: Descritores

class Validado:
    def __set_name__(self, dono, nome):
        self.nome_publico = nome
        self.nome_privado = "_" + nome

    def __get__(self, obj, tipo=None):
        if obj is None:
            return self
        return getattr(obj, self.nome_privado)

    def __set__(self, obj, valor):
        self.validar(valor)
        setattr(obj, self.nome_privado, valor)

    def validar(self, valor):
        pass

class Positivo(Validado):
    def validar(self, valor):
        if not isinstance(valor, (int, float)) or valor <= 0:
            raise ValueError(f"{self.nome_publico} deve ser um número > 0")

class TextoNaoVazio(Validado):
    def __init__(self, maximo=100):
        self.maximo = maximo
    def validar(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError(f"{self.nome_publico} não pode estar vazio")
        if len(valor) > self.maximo:
            raise ValueError(f"{self.nome_publico}: máximo {self.maximo}")

class Produto:
    nome = TextoNaoVazio(maximo=40)
    preco = Positivo()
    stock = Positivo()

    def __init__(self, nome, preco, stock):
        self.nome, self.preco, self.stock = nome, preco, stock

p = Produto("Lâmpada LED", 4.99, 200)
print(p.nome, p.preco)
for campo, valor in [("preco", -1), ("nome", "  "), ("stock", "muito")]:
    try:
        setattr(p, campo, valor)
    except ValueError as e:
        print("Recusado:", e)
