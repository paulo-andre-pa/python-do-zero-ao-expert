# Capítulo 19 — Metaprogramação: gestores de contexto, descritores e metaclasses
# Secção: Gestores de contexto

import sqlite3
from contextlib import contextmanager

@contextmanager
def transacao(con):
    try:
        yield con.cursor()
        con.commit()
    except Exception:
        con.rollback()
        raise

con = sqlite3.connect(":memory:")
con.execute("CREATE TABLE contas (titular TEXT, "
            "saldo REAL CHECK (saldo >= 0))")
con.executemany("INSERT INTO contas VALUES (?, ?)", [("A", 100), ("B", 50)])
con.commit()
try:
    with transacao(con) as cur:
        sql = "UPDATE contas SET saldo = saldo + ? WHERE titular = ?"
        cur.execute(sql, (80, "B"))
        cur.execute(sql, (-80, "A"))
        cur.execute(sql, (-80, "A"))       # deixaria A negativo
except sqlite3.IntegrityError:
    print("Transferência anulada")
print(con.execute("SELECT * FROM contas").fetchall())
