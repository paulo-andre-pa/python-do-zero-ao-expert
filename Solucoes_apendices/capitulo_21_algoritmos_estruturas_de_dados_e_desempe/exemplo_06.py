# Capítulo 21 — Algoritmos, estruturas de dados e desempenho
# Secção: Grafos

import heapq

estradas = {   # cidade -> {vizinha: km}
    "Lisboa": {"Santarém": 85, "Setúbal": 50, "Évora": 135},
    "Santarém": {"Lisboa": 85, "Coimbra": 140, "Évora": 115},
    "Setúbal": {"Lisboa": 50, "Évora": 100},
    "Évora": {"Lisboa": 135, "Santarém": 115, "Setúbal": 100},
    "Coimbra": {"Santarém": 140, "Porto": 120},
    "Porto": {"Coimbra": 120},
}

def dijkstra(grafo, origem):
    dist = {origem: 0}
    anterior = {origem: None}
    fila = [(0, origem)]
    while fila:
        d, no = heapq.heappop(fila)
        if d > dist[no]:
            continue                       # entrada desatualizada
        for viz, custo in grafo[no].items():
            nova = d + custo
            if nova < dist.get(viz, float("inf")):
                dist[viz], anterior[viz] = nova, no
                heapq.heappush(fila, (nova, viz))
    return dist, anterior

dist, ant = dijkstra(estradas, "Setúbal")
rota, no = [], "Porto"
while no:
    rota.append(no); no = ant[no]
print(" -> ".join(reversed(rota)), f"({dist['Porto']} km)")
