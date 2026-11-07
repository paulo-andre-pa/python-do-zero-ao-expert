# Capítulo 12 — POO avançada: herança, dataclasses e métodos especiais
# Secção: Herança

class Funcionario:
    def __init__(self, nome, salario_base):
        self.nome = nome
        self.salario_base = salario_base

    def salario(self):
        return self.salario_base

    def __repr__(self):
        return f"{type(self).__name__}({self.nome!r}, {self.salario():.2f})"

class Gestor(Funcionario):
    def __init__(self, nome, salario_base, equipa=None):
        super().__init__(nome, salario_base)    # reutiliza o construtor
        self.equipa = equipa or []

    def salario(self):                          # redefine
        return super().salario() + 150 * len(self.equipa)

class Comercial(Funcionario):
    def __init__(self, nome, salario_base, vendas=0.0):
        super().__init__(nome, salario_base)
        self.vendas = vendas

    def salario(self):
        return self.salario_base + 0.05 * self.vendas

ana = Funcionario("Ana", 1400)
rui = Comercial("Rui", 1100, vendas=18_000)
eva = Gestor("Eva", 2200, equipa=[ana, rui])
for f in (ana, rui, eva):
    print(f)
print(isinstance(eva, Funcionario), issubclass(Comercial, Funcionario))
