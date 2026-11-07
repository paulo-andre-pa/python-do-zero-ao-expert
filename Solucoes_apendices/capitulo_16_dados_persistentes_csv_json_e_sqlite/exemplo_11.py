# Capítulo 16 — Dados persistentes: CSV, JSON e SQLite
# Secção: O padrão repositório

import csv, json, sqlite3

con = sqlite3.connect(":memory:")
con.execute("""CREATE TABLE vendas (data TEXT, loja TEXT, produto TEXT,
               quantidade INTEGER, preco REAL)""")
with open("vendas.csv", newline="", encoding="utf-8") as f, con:
    linhas = [(l["data"], l["loja"], l["produto"],
               int(l["quantidade"]), float(l["preco"]))
              for l in csv.DictReader(f, delimiter=";")]
    con.executemany("INSERT INTO vendas VALUES (?, ?, ?, ?, ?)", linhas)

por_loja = con.execute("""
    SELECT loja, ROUND(SUM(quantidade * preco), 2) FROM vendas
    GROUP BY loja ORDER BY 2 DESC""").fetchall()
top = con.execute("""
    SELECT produto, SUM(quantidade) AS u FROM vendas
    GROUP BY produto ORDER BY u DESC LIMIT 1""").fetchone()

for loja, total in por_loja:
    print(f"{loja:<8}{total:>8.2f} €")
print("Mais vendido:", top)
with open("relatorio.json", "w", encoding="utf-8") as f:
    json.dump(dict(por_loja), f, ensure_ascii=False, indent=2)
print(open("relatorio.json", encoding="utf-8").read())
