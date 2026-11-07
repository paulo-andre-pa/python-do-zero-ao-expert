"""Executa, por ordem, todos os exemplos do Capítulo 3 — Texto: trabalhar com strings.

Os exemplos de um capítulo partilham definições, por isso são executados
num mesmo espaço de nomes, tal como no livro. Os ficheiros *_ilustrativo.py
não são executados (exigem pacotes ou serviços externos).
"""
import os
import pathlib

pasta = pathlib.Path(__file__).resolve().parent
os.chdir(pasta)
espaco = {"__name__": "__main__"}
for ficheiro in sorted(pasta.glob("exemplo_*.py")):
    if ficheiro.stem.endswith("_ilustrativo"):
        continue
    print(f"\n=== {ficheiro.name} ===")
    try:
        exec(compile(ficheiro.read_text(encoding="utf-8"), ficheiro.name,
                     "exec"), espaco)
    except Exception as erro:          # alguns exemplos falham de propósito
        print(f"{type(erro).__name__}: {erro}")
