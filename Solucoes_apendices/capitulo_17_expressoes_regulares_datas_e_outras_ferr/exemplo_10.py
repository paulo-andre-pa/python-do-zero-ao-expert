# Capítulo 17 — Expressões regulares, datas e outras ferramentas essenciais
# Secção: Automatizar ficheiros: shutil e zipfile

import shutil, zipfile
from pathlib import Path

origem = Path("projeto")
(origem / "docs").mkdir(parents=True, exist_ok=True)
(origem / "main.py").write_text("print('olá')\n", encoding="utf-8")
(origem / "docs" / "manual.md").write_text("# Manual\n", encoding="utf-8")

shutil.copytree(origem, "projeto_copia", dirs_exist_ok=True)
arquivo = shutil.make_archive("backup_projeto", "zip", origem)
with zipfile.ZipFile(arquivo) as z:
    print(sorted(z.namelist()))
print(Path(arquivo).name, Path(arquivo).stat().st_size > 0)
