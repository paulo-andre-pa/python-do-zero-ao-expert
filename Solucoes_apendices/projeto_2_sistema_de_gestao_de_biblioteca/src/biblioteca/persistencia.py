"""Guardar e carregar o estado da biblioteca em JSON."""
import json
from dataclasses import asdict
from datetime import date
from pathlib import Path

from biblioteca.dominio import Emprestimo, Livro, Socio, TipoSocio
from biblioteca.servico import Biblioteca

def _converter(obj):
    if isinstance(obj, date):
        return obj.isoformat()
    if isinstance(obj, TipoSocio):
        return obj.name
    raise TypeError(type(obj).__name__)

def guardar(bib: Biblioteca, caminho: Path) -> None:
    dados = {"livros": [asdict(l) for l in bib.livros.values()],
             "socios": [asdict(s) for s in bib.socios.values()],
             "emprestimos": [asdict(e) for e in bib.emprestimos]}
    texto = json.dumps(dados, default=_converter, ensure_ascii=False,
                       indent=1)
    caminho.write_text(texto, encoding="utf-8")

def _data(texto: str | None) -> date | None:
    return date.fromisoformat(texto) if texto else None

def carregar(caminho: Path) -> Biblioteca:
    dados = json.loads(caminho.read_text(encoding="utf-8"))
    bib = Biblioteca()
    for l in dados["livros"]:
        bib.adicionar_livro(Livro(**l))
    for s in dados["socios"]:
        tipo = TipoSocio[s["tipo"]]
        bib.socios[s["numero"]] = Socio(**{**s, "tipo": tipo})
    for e in dados["emprestimos"]:
        bib.emprestimos.append(Emprestimo(
            e["isbn"], e["socio"], _data(e["saida"]), _data(e["prevista"]),
            _data(e["devolucao"])))
    return bib
