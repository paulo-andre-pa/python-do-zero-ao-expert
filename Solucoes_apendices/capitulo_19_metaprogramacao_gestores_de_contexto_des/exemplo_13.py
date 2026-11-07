# Capítulo 19 — Metaprogramação: gestores de contexto, descritores e metaclasses
# Secção: Introspeção

import sqlite3

class Campo:
    tipo_sql = "TEXT"
    def __set_name__(self, dono, nome):
        self.nome = nome
    def __get__(self, obj, tipo=None):
        return self if obj is None else obj.__dict__.get(self.nome)
    def __set__(self, obj, valor):
        obj.__dict__[self.nome] = self.converter(valor)
    def converter(self, v):
        return v

class Inteiro(Campo):
    tipo_sql = "INTEGER"
    def converter(self, v):
        return int(v)

class Texto(Campo):
    def converter(self, v):
        if not str(v).strip():
            raise ValueError(f"{self.nome} vazio")
        return str(v).strip()

class Decimal(Campo):
    tipo_sql = "REAL"
    def converter(self, v):
        return round(float(v), 2)

class Modelo:
    def __init_subclass__(cls, tabela: str, **kw):
        super().__init_subclass__(**kw)
        cls._tabela = tabela
        cls._campos = [n for n, v in vars(cls).items()
                       if isinstance(v, Campo)]

    def __init__(self, **valores):
        for nome in self._campos:
            setattr(self, nome, valores[nome])

    @classmethod
    def sql_criar(cls):
        cols = ", ".join(f"{n} {getattr(cls, n).tipo_sql}"
                         for n in cls._campos)
        return f"CREATE TABLE {cls._tabela} ({cols})"

    def inserir(self, con):
        marcadores = ", ".join("?" * len(self._campos))
        con.execute(f"INSERT INTO {self._tabela} VALUES ({marcadores})",
                    [getattr(self, n) for n in self._campos])

class Livro(Modelo, tabela="livros"):
    isbn = Texto()
    titulo = Texto()
    ano = Inteiro()
    preco = Decimal()

con = sqlite3.connect(":memory:")
print(Livro.sql_criar())
con.execute(Livro.sql_criar())
Livro(isbn="978-0", titulo=" Python Prático ", ano="2026",
      preco=29.899).inserir(con)
print(con.execute("SELECT * FROM livros").fetchall())
