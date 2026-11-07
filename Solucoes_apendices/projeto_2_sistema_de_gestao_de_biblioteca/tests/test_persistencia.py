from datetime import timedelta
from biblioteca.persistencia import carregar, guardar
from conftest import DIA

def test_guardar_e_carregar_preserva_tudo(bib, tmp_path):
    bib.emprestar("111", 1, DIA)
    bib.devolver("111", 1, DIA + timedelta(days=20))
    bib.emprestar("333", 2, DIA)
    ficheiro = tmp_path / "biblioteca.json"
    guardar(bib, ficheiro)
    copia = carregar(ficheiro)
    assert copia.livros == bib.livros
    assert copia.socios == bib.socios
    assert copia.emprestimos == bib.emprestimos
