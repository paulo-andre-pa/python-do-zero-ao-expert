# Capítulo 16 — Dados persistentes: CSV, JSON e SQLite
# Secção: O padrão repositório

import sqlite3
from dataclasses import dataclass

@dataclass
class Contacto:
    nome: str
    email: str
    telefone: str = ""
    id: int | None = None

class RepositorioContactos:
    def __init__(self, caminho=":memory:"):
        self.con = sqlite3.connect(caminho)
        self.con.row_factory = sqlite3.Row
        self.con.execute("""CREATE TABLE IF NOT EXISTS contactos (
            id INTEGER PRIMARY KEY, nome TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL, telefone TEXT)""")

    def adicionar(self, c: Contacto) -> Contacto:
        with self.con:
            cur = self.con.execute(
                "INSERT INTO contactos (nome, email, telefone) "
                "VALUES (?, ?, ?)", (c.nome, c.email, c.telefone))
        c.id = cur.lastrowid
        return c

    def procurar(self, termo: str) -> list[Contacto]:
        linhas = self.con.execute(
            "SELECT * FROM contactos WHERE nome LIKE ? ORDER BY nome",
            (f"%{termo}%",))
        return [Contacto(l["nome"], l["email"], l["telefone"], l["id"])
                for l in linhas]

    def remover(self, id_: int) -> bool:
        with self.con:
            cur = self.con.execute("DELETE FROM contactos WHERE id = ?",
                                   (id_,))
        return cur.rowcount == 1

repo = RepositorioContactos()       # em memória: ideal para testes
repo.adicionar(Contacto("Marta Reis", "marta@ex.pt", "912000111"))
repo.adicionar(Contacto("Mário Lopes", "mario@ex.pt"))
repo.adicionar(Contacto("Rita Sousa", "rita@ex.pt"))
print([c.nome for c in repo.procurar("Mar")])
print(repo.remover(2), [c.nome for c in repo.procurar("")])
