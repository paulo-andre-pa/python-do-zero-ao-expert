# Capítulo 7 — Dicionários e conjuntos
# Secção: Porque são tão rápidos?

import timeit

dados_lista = list(range(100_000))
dados_set = set(dados_lista)
t_lista = timeit.timeit(lambda: 99_999 in dados_lista, number=200)
t_set = timeit.timeit(lambda: 99_999 in dados_set, number=200)
print(f"O conjunto foi cerca de {t_lista / t_set:,.0f} vezes mais rápido")
