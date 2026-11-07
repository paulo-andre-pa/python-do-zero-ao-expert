def preco_com_iva(preco: float, taxa: float = 0.23) -> float:
    if preco < 0:
        raise ValueError("preço negativo")
    return round(preco * (1 + taxa), 2)

def aplicar_desconto(preco: float, percentagem: float) -> float:
    if not 0 <= percentagem <= 100:
        raise ValueError("percentagem inválida")
    return round(preco * (1 - percentagem / 100), 2)
