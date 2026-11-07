# Capítulo 17 — Expressões regulares, datas e outras ferramentas essenciais
# Secção: Mais estruturas de dados

import re, shutil
from datetime import date, datetime
from pathlib import Path

CATEGORIAS = {
    "Documentos": {".pdf", ".docx", ".txt", ".md"},
    "Imagens": {".jpg", ".jpeg", ".png", ".gif"},
    "Folhas": {".xlsx", ".csv", ".ods"},
    "Arquivos": {".zip", ".rar", ".7z"},
}
PADROES_DATA = [(re.compile(r"(\d{4})-(\d{2})-(\d{2})"), "amd"),
                (re.compile(r"(\d{2})-(\d{2})-(\d{4})"), "dma")]

def categoria(ficheiro: Path) -> str:
    ext = ficheiro.suffix.lower()
    return next((c for c, exts in CATEGORIAS.items() if ext in exts),
                "Outros")

def data_do_ficheiro(ficheiro: Path) -> date:
    for padrao, ordem in PADROES_DATA:
        if m := padrao.search(ficheiro.stem):
            a, b, c = map(int, m.groups())
            try:
                return date(a, b, c) if ordem == "amd" else date(c, b, a)
            except ValueError:
                pass                     # p. ex. 2026-13-45
    return datetime.fromtimestamp(ficheiro.stat().st_mtime).date()

def destino_livre(caminho: Path) -> Path:
    n = 1
    while caminho.exists():
        caminho = caminho.with_stem(f"{caminho.stem} ({n})")
        n += 1
    return caminho

def organizar(pasta: Path, ensaio=True):
    for f in sorted(p for p in pasta.iterdir() if p.is_file()):
        d = data_do_ficheiro(f)
        pasta_mes = pasta / categoria(f) / f"{d:%Y-%m}"
        destino = destino_livre(pasta_mes / f.name)
        print(f"{'[ensaio] ' if ensaio else ''}{f.name} -> "
              f"{destino.relative_to(pasta)}")
        if not ensaio:
            destino.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(f, destino)

downloads = Path("downloads")
downloads.mkdir(exist_ok=True)
for nome in ["fatura_2026-03-15.pdf", "foto 24-12-2025.jpg",
             "vendas_2026-10-01.xlsx", "programa.zip"]:
    (downloads / nome).touch()
organizar(downloads, ensaio=False)
print(sorted(str(p.relative_to(downloads)) for p in downloads.rglob("*.*")))
