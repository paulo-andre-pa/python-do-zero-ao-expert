# Apêndice B — Soluções de exercícios selecionados
# Secção: Capítulo 4 — Decisões

def calcular(expressao: str) -> float | str:
    match expressao.split():
        case [a, "+", b]:
            return float(a) + float(b)
        case [a, "-", b]:
            return float(a) - float(b)
        case [a, "*", b]:
            return float(a) * float(b)
        case [_, "/", "0"]:
            return "erro: divisão por zero"
        case [a, "/", b]:
            return float(a) / float(b)
        case [a, "^", b]:
            return float(a) ** float(b)
        case _:
            return "erro: expressão inválida"

for e in ["3 + 4", "10 / 2", "2 ^ 8", "5 / 0", "2 +"]:
    print(f"{e:<8} = {calcular(e)}")
