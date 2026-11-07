"""Funções de conversão de unidades."""

KM_POR_MILHA = 1.609344

def celsius_para_fahrenheit(c):
    return c * 9 / 5 + 32

def milhas_para_km(milhas):
    return milhas * KM_POR_MILHA

def _arredondar(x):
    """Função interna (o _ indica uso privado)."""
    return round(x, 2)
