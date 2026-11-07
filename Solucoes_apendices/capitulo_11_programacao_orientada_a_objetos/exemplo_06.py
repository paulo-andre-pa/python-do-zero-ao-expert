# Capítulo 11 — Programação orientada a objetos
# Secção: Atributos de classe

class Funcionario:
    empresa = "TecnoSul, Lda."      # atributo de classe
    total = 0

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
        Funcionario.total += 1
        self.numero = Funcionario.total

f1 = Funcionario("Inês", 1800)
f2 = Funcionario("Paulo", 2100)
print(f1.empresa, f2.numero, Funcionario.total)
