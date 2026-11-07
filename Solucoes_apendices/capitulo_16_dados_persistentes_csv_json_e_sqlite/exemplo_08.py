# Capítulo 16 — Dados persistentes: CSV, JSON e SQLite
# Secção: SQLite: uma base de dados completa num ficheiro

try:
    with con:
        con.execute("UPDATE produtos SET preco = preco * 0.9 "
                    "WHERE categoria = ?", ("Mobiliário",))
        con.execute("INSERT INTO produtos (nome, categoria, preco) "
                    "VALUES (?, ?, ?)", ("Rato óptico", "Informática", 9.9))
except sqlite3.IntegrityError as e:
    print("Transação anulada:", e)

preco = con.execute("SELECT preco FROM produtos WHERE id = 3").fetchone()[0]
print("Preço da cadeira (inalterado):", preco)
