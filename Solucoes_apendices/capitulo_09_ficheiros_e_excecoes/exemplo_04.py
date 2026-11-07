# Capítulo 9 — Ficheiros e exceções
# Secção: Caminhos com pathlib

from pathlib import Path

pasta = Path("relatorios") / "2026"     # o operador / junta caminhos
pasta.mkdir(parents=True, exist_ok=True)

ficheiro = pasta / "marco.txt"
ficheiro.write_text("Vendas de março: 12 430 €\n", encoding="utf-8")
print(ficheiro.read_text(encoding="utf-8").strip())
print(ficheiro.name, ficheiro.stem, ficheiro.suffix, ficheiro.parent)
print(ficheiro.exists(), ficheiro.is_file(), pasta.is_dir())
