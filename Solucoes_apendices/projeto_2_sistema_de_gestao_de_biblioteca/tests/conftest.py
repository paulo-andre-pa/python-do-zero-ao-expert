from datetime import date
import pytest
from biblioteca import Biblioteca, Livro, TipoSocio

DIA = date(2026, 3, 2)

@pytest.fixture
def bib():
    b = Biblioteca()
    b.adicionar_livro(Livro("111", "Python Avançado", "M. Lopes", 2024, 2))
    b.adicionar_livro(Livro("222", "Redes", "A. Reis", 2021))
    b.adicionar_livro(Livro("333", "Bases de Dados", "C. Dias", 2023))
    b.adicionar_livro(Livro("444", "Algoritmos", "R. Sousa", 2020))
    b.inscrever(1, "Ana", TipoSocio.ESTUDANTE)
    b.inscrever(2, "Prof. Rui", TipoSocio.DOCENTE)
    b.inscrever(3, "Eva", TipoSocio.EXTERNO)
    return b
