# Capítulo 16 — Dados persistentes: CSV, JSON e SQLite
# Secção: SQLite: uma base de dados completa num ficheiro

con.row_factory = sqlite3.Row      # linhas acessíveis por nome de coluna

for p in con.execute("SELECT nome, preco FROM produtos "
                     "WHERE preco > ? ORDER BY preco DESC", (100,)):
    print(f"{p['nome']:<20}{p['preco']:>8.2f}")
