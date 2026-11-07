# Capítulo 21 — Algoritmos, estruturas de dados e desempenho
# Secção: Grafos

from collections import deque

metro = {
    "Aliados": ["Trindade", "S. Bento"],
    "Trindade": ["Aliados", "Bolhão", "Lapa", "Campanhã"],
    "S. Bento": ["Aliados", "Jardim do Morro"],
    "Bolhão": ["Trindade", "Campanhã"],
    "Lapa": ["Trindade", "Casa da Música"],
    "Casa da Música": ["Lapa"],
    "Campanhã": ["Trindade", "Bolhão"],
    "Jardim do Morro": ["S. Bento"],
}

def caminho_mais_curto(grafo, origem, destino):
    anterior = {origem: None}
    fila = deque([origem])
    while fila:
        no = fila.popleft()
        if no == destino:
            caminho = []
            while no is not None:
                caminho.append(no)
                no = anterior[no]
            return caminho[::-1]
        for vizinho in grafo[no]:
            if vizinho not in anterior:
                anterior[vizinho] = no
                fila.append(vizinho)
    return None

print(" -> ".join(caminho_mais_curto(metro, "Casa da Música",
                                      "Jardim do Morro")))
