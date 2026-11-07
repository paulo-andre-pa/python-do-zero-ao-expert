# Apêndice C — Preparação para entrevistas técnicas
# Secção: Exercícios típicos (com soluções)

def juntar(intervalos: list[tuple[int, int]]) -> list[tuple[int, int]]:
    resultado: list[tuple[int, int]] = []
    for inicio, fim in sorted(intervalos):
        if resultado and inicio <= resultado[-1][1]:
            resultado[-1] = (resultado[-1][0], max(resultado[-1][1], fim))
        else:
            resultado.append((inicio, fim))
    return resultado

print(juntar([(9, 11), (14, 15), (10, 12), (15, 17), (1, 2)]))
