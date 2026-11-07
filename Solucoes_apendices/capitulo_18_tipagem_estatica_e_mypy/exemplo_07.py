# Capítulo 18 — Tipagem estática e mypy
# Secção: Genéricos

def primeiro[T](itens: list[T]) -> T | None:
    return itens[0] if itens else None

def maior_por[T](itens: list[T], chave: Callable[[T], float]) -> T:
    return max(itens, key=chave)

x = primeiro([3, 1, 2])          # o verificador infere: int | None
nome = primeiro(["Eva", "Rui"])  # str | None
print(x, nome, maior_por(["ab", "abcd", "abc"], len))
