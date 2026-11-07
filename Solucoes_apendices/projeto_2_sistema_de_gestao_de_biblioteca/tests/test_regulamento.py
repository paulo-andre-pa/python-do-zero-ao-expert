from datetime import timedelta
import pytest
from biblioteca.erros import (EmprestimoDuplicado, LimiteAtingido,
                              LivroIndisponivel, SocioImpedido)
from conftest import DIA

@pytest.mark.parametrize("socio, dias", [(1, 14), (2, 30), (3, 7)])
def test_r1_prazo_por_tipo(bib, socio, dias):
    e = bib.emprestar("111", socio, DIA)
    assert (e.prevista - e.saida).days == dias

def test_r1_limite_externo(bib):
    bib.emprestar("111", 3, DIA)
    bib.emprestar("222", 3, DIA)
    with pytest.raises(LimiteAtingido):
        bib.emprestar("333", 3, DIA)

def test_r2_exemplares(bib):
    bib.emprestar("111", 1, DIA)
    bib.emprestar("111", 2, DIA)
    assert bib.disponiveis("111") == 0
    with pytest.raises(LivroIndisponivel):
        bib.emprestar("111", 3, DIA)

def test_r3_mesmo_livro_duas_vezes(bib):
    bib.emprestar("111", 1, DIA)
    with pytest.raises(EmprestimoDuplicado):
        bib.emprestar("111", 1, DIA)

@pytest.mark.parametrize("dias_depois, multa", [
    (14, 0.0), (15, 0.5), (24, 5.0), (100, 15.0)])
def test_r4_multas(bib, dias_depois, multa):
    bib.emprestar("222", 1, DIA)
    devolucao = DIA + timedelta(days=dias_depois)
    assert bib.devolver("222", 1, devolucao) == multa

def test_r5_impedido_por_multas(bib):
    bib.emprestar("222", 1, DIA)
    bib.devolver("222", 1, DIA + timedelta(days=30))   # 8 € de multa
    with pytest.raises(SocioImpedido, match="multas"):
        bib.emprestar("333", 1, DIA + timedelta(days=31))
    bib.pagar(1, 8)
    bib.emprestar("333", 1, DIA + timedelta(days=31))

def test_r5_impedido_por_atraso(bib):
    bib.emprestar("222", 3, DIA)
    with pytest.raises(SocioImpedido, match="atraso"):
        bib.emprestar("333", 3, DIA + timedelta(days=8))

def test_r6_atrasados_e_ranking(bib):
    bib.emprestar("111", 1, DIA)
    bib.emprestar("111", 2, DIA)
    assert [e.socio for e in bib.atrasados(DIA + timedelta(days=20))] == [1]
    assert bib.mais_requisitados(1) == [("Python Avançado", 2)]
