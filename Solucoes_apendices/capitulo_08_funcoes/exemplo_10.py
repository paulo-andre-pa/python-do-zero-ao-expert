# Capítulo 8 — Funções
# Secção: Documentar: docstrings e anotações

def juros_compostos(capital: float, taxa: float, anos: int) -> float:
    """Calcula o capital acumulado com juros compostos.

    Args:
        capital: valor inicial investido, em euros.
        taxa: taxa de juro anual (0.03 significa 3 %).
        anos: número de anos do investimento.

    Returns:
        O capital final, arredondado ao cêntimo.
    """
    return round(capital * (1 + taxa) ** anos, 2)

print(juros_compostos(1000, 0.03, 10))
print(juros_compostos.__doc__.splitlines()[0])
