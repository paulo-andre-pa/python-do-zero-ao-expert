# Capítulo 16 — Dados persistentes: CSV, JSON e SQLite
# Secção: SQLite: uma base de dados completa num ficheiro

nome_digitado = "x' OR '1'='1"
perigoso = f"SELECT nome FROM produtos WHERE nome = '{nome_digitado}'"
print(perigoso)
print("Linhas devolvidas:", len(con.execute(perigoso).fetchall()))

seguro = con.execute("SELECT nome FROM produtos WHERE nome = ?",
                     (nome_digitado,)).fetchall()
print("Com parâmetros:", len(seguro))
