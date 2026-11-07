# Capítulo 11 — Programação orientada a objetos
# Secção: Métodos de classe e métodos estáticos

from datetime import date

class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self.nome = nome
        self.ano_nascimento = ano_nascimento

    @classmethod
    def de_texto(cls, texto):
        """Cria uma Pessoa a partir de 'Nome;Ano'."""
        nome, ano = texto.split(";")
        return cls(nome.strip(), int(ano))

    @staticmethod
    def ano_valido(ano):
        return 1900 <= ano <= date.today().year

    def idade_em(self, ano):
        return ano - self.ano_nascimento

p = Pessoa.de_texto("Clara Sousa; 1995")
print(p.nome, p.idade_em(2026), Pessoa.ano_valido(1850))
