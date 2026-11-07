"""Interface de linha de comandos: python -m tarefas <comando>."""
import argparse
import os
import sys
from pathlib import Path

from tarefas.repositorio import RepositorioTarefas
from tarefas.servicos import GestorTarefas, TarefaInexistente

BD_OMISSAO = Path.home() / ".tarefas.db"
SIMBOLO = {1: "!!!", 2: "!!", 3: "!"}

def criar_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="tarefas",
                                description="Gestor de tarefas.")
    sub = p.add_subparsers(dest="comando", required=True)

    a = sub.add_parser("add", help="adicionar uma tarefa")
    a.add_argument("titulo")
    a.add_argument("-p", "--prioridade", default="media")
    a.add_argument("--prazo", help="AAAA-MM-DD, hoje, amanha ou +N")
    a.add_argument("-e", "--etiquetas", default="",
                   help="separadas por vírgulas")

    ls = sub.add_parser("ls", help="listar tarefas")
    ls.add_argument("-t", "--todas", action="store_true")
    ls.add_argument("-e", "--etiqueta")

    for nome, ajuda in (("feito", "concluir"), ("rm", "remover")):
        s = sub.add_parser(nome, help=f"{ajuda} uma tarefa")
        s.add_argument("id", type=int)

    sub.add_parser("stats", help="estatísticas")
    return p

def mostrar(gestor: GestorTarefas, tarefas) -> None:
    if not tarefas:
        print("Nada a fazer. Bom trabalho!")
        return
    hoje = gestor.hoje()
    for t in tarefas:
        marca = "x" if t.concluida else ("A" if t.atrasada(hoje) else " ")
        prazo = t.prazo.strftime("%d/%m") if t.prazo else "--/--"
        etiq = " ".join(f"#{e}" for e in t.etiquetas)
        print(f"[{marca}] {t.id:>3}  {SIMBOLO[t.prioridade]:<4}{prazo}  "
              f"{t.titulo} {etiq}".rstrip())

def executar(args: argparse.Namespace, gestor: GestorTarefas) -> None:
    match args.comando:
        case "add":
            t = gestor.adicionar(args.titulo, args.prioridade, args.prazo,
                                 args.etiquetas)
            print(f"Tarefa {t.id} criada.")
        case "ls":
            mostrar(gestor, gestor.listar(args.todas, args.etiqueta))
        case "feito":
            print(f"Concluída: {gestor.concluir(args.id).titulo}")
        case "rm":
            gestor.remover(args.id)
            print(f"Tarefa {args.id} removida.")
        case "stats":
            for chave, valor in gestor.estatisticas().items():
                print(f"{chave.replace('_', ' '):<20}{valor:>4}")

def main(argv: list[str] | None = None,
         gestor: GestorTarefas | None = None) -> int:
    args = criar_parser().parse_args(argv)
    if gestor is None:
        caminho = os.environ.get("TAREFAS_BD", str(BD_OMISSAO))
        gestor = GestorTarefas(RepositorioTarefas(caminho))
    try:
        executar(args, gestor)
    except (ValueError, TarefaInexistente) as erro:
        print(f"erro: {erro}", file=sys.stderr)
        return 1
    return 0
