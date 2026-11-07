# Capítulo 9 — Ficheiros e exceções
# Secção: Caminhos com pathlib

for nome in ["abril.txt", "maio.txt", "resumo.csv"]:
    (pasta / nome).write_text("...", encoding="utf-8")

for f in sorted(pasta.glob("*.txt")):
    print(f.name, f.stat().st_size, "bytes")
