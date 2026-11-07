SIMBOLOS = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]

def para_romano(n: int) -> str:
    if not 1 <= n <= 3999:
        raise ValueError("só números entre 1 e 3999")
    resultado = []
    for valor, simbolo in SIMBOLOS:
        quantidade, n = divmod(n, valor)
        resultado.append(simbolo * quantidade)
    return "".join(resultado)
