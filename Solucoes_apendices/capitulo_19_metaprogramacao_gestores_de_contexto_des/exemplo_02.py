# Capítulo 19 — Metaprogramação: gestores de contexto, descritores e metaclasses
# Secção: Gestores de contexto

from contextlib import contextmanager
import os

@contextmanager
def pasta_de_trabalho(caminho):
    anterior = os.getcwd()
    os.makedirs(caminho, exist_ok=True)
    os.chdir(caminho)
    try:
        yield caminho
    finally:
        os.chdir(anterior)       # restaura sempre

with pasta_de_trabalho("temporaria"):
    print("dentro:", os.path.basename(os.getcwd()))
print("fora:", os.path.basename(os.getcwd()) != "temporaria")
