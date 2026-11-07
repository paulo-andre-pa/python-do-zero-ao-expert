# Apêndice B — Soluções de exercícios selecionados
# Secção: Capítulo 6 — Listas e tuplos

def rodar(lista: list, k: int) -> list:
    if not lista:
        return []
    k %= len(lista)
    return lista[-k:] + lista[:-k] if k else lista[:]

print(rodar([1, 2, 3, 4, 5], 2), rodar([1, 2, 3], 7), rodar([], 3))
