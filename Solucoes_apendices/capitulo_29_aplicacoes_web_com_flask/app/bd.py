import sqlite3
from flask import current_app, g

ESQUEMA = """
CREATE TABLE IF NOT EXISTS utilizadores (
    id INTEGER PRIMARY KEY, nome TEXT UNIQUE NOT NULL, hash TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS tarefas (
    id INTEGER PRIMARY KEY,
    dono INTEGER NOT NULL REFERENCES utilizadores(id),
    titulo TEXT NOT NULL, feita INTEGER NOT NULL DEFAULT 0);
"""

def obter():
    """Uma ligação por pedido, guardada no objeto g do Flask."""
    if "bd" not in g:
        g.bd = sqlite3.connect(current_app.config["BASE_DADOS"])
        g.bd.row_factory = sqlite3.Row
        g.bd.executescript(ESQUEMA)
    return g.bd

def fechar(_erro=None):
    bd = g.pop("bd", None)
    if bd is not None:
        bd.close()

def registar(app):
    app.teardown_appcontext(fechar)    # fecha no fim de cada pedido
