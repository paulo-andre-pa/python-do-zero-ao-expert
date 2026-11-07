# Projeto 2 — Sistema de gestão de biblioteca
# Secção: Utilização

import os, sys
sys.path.insert(0, os.path.abspath("src"))
from datetime import date, timedelta
from biblioteca import Biblioteca, ErroBiblioteca, Livro, TipoSocio

bib = Biblioteca()
for isbn, titulo, autor, ano, ex in [
        ("978-1", "Introdução à Programação", "J. Matos", 2022, 3),
        ("978-2", "Estruturas de Dados", "L. Faria", 2019, 1),
        ("978-3", "Engenharia de Software", "P. Costa", 2024, 2)]:
    bib.adicionar_livro(Livro(isbn, titulo, autor, ano, ex))
bib.inscrever(101, "Beatriz", TipoSocio.ESTUDANTE)
bib.inscrever(102, "Dr. Nuno", TipoSocio.DOCENTE)
bib.inscrever(103, "Carla", TipoSocio.EXTERNO)

d = date(2026, 4, 1)
operacoes = [("emp", "978-2", 101, 0), ("emp", "978-2", 102, 1),
             ("emp", "978-1", 103, 2), ("emp", "978-3", 102, 3),
             ("dev", "978-2", 101, 20), ("emp", "978-1", 103, 21),
             ("dev", "978-1", 103, 25), ("emp", "978-2", 101, 26)]
for op, isbn, socio, dia in operacoes:
    hoje = d + timedelta(days=dia)
    try:
        if op == "emp":
            e = bib.emprestar(isbn, socio, hoje)
            print(f"{hoje:%d/%m} empréstimo {isbn} a {socio}, "
                  f"devolver até {e.prevista:%d/%m}")
        else:
            multa = bib.devolver(isbn, socio, hoje)
            print(f"{hoje:%d/%m} devolução {isbn} de {socio}: "
                  f"multa {multa:.2f} €")
    except ErroBiblioteca as erro:
        print(f"{hoje:%d/%m} RECUSADO ({type(erro).__name__}): {erro}")

print("Atrasados a 30/04:",
      [(e.isbn, e.socio) for e in bib.atrasados(date(2026, 4, 30))])
print("Mais requisitados:", bib.mais_requisitados(2))
