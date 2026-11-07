# Capítulo 16 — Dados persistentes: CSV, JSON e SQLite
# Secção: SQLite: uma base de dados completa num ficheiro

import sqlite3

con = sqlite3.connect("loja.db")       # cria o ficheiro se não existir
con.execute("PRAGMA foreign_keys = ON")
con.executescript("""
DROP TABLE IF EXISTS vendas;
DROP TABLE IF EXISTS produtos;
CREATE TABLE produtos (
    id        INTEGER PRIMARY KEY AUTOINCREMENT,
    nome      TEXT NOT NULL UNIQUE,
    categoria TEXT NOT NULL,
    preco     REAL NOT NULL CHECK (preco >= 0)
);
CREATE TABLE vendas (
    id         INTEGER PRIMARY KEY,
    produto_id INTEGER NOT NULL REFERENCES produtos(id),
    quantidade INTEGER NOT NULL,
    data       TEXT NOT NULL
);
""")

produtos = [("Portátil 14''", "Informática", 749.0),
            ("Rato óptico", "Informática", 12.9),
            ("Cadeira ergonómica", "Mobiliário", 189.0),
            ("Secretária", "Mobiliário", 239.0)]
con.executemany(
    "INSERT INTO produtos (nome, categoria, preco) VALUES (?, ?, ?)",
    produtos)
vendas = [(1, 3, "2026-03-01"), (2, 10, "2026-03-01"), (3, 2, "2026-03-02"),
          (1, 1, "2026-03-03"), (4, 1, "2026-03-03"), (2, 5, "2026-03-04")]
con.executemany(
    "INSERT INTO vendas (produto_id, quantidade, data) VALUES (?, ?, ?)",
    vendas)
con.commit()
print(con.execute("SELECT COUNT(*) FROM vendas").fetchone()[0], "vendas")
