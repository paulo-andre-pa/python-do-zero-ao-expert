# Capítulo 21 — Algoritmos, estruturas de dados e desempenho
# Secção: Medir antes de otimizar

import timeit

setup = "dados = list(range(10_000))"
casos = {
    "ciclo com append": "r = []\nfor x in dados: r.append(x * 2)",
    "compreensão": "r = [x * 2 for x in dados]",
    "map com lambda": "r = list(map(lambda x: x * 2, dados))",
}
for nome, codigo in casos.items():
    t = min(timeit.repeat(codigo, setup, number=200, repeat=3))
    print(f"{nome:<18}{t * 1000 / 200:7.3f} ms por execução")
