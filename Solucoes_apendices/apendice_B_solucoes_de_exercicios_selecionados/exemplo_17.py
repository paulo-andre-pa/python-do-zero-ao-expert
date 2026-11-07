# Apêndice B — Soluções de exercícios selecionados
# Secção: Capítulo 21 — Algoritmos

from collections import deque

def ordem_topologica(dependencias: dict[str, set[str]]) -> list[str]:
    """dependencias[t] = tarefas que têm de ser feitas antes de t."""
    tarefas = set(dependencias) | set().union(*dependencias.values())
    faltam = {t: len(dependencias.get(t, ())) for t in tarefas}
    seguintes = {t: [] for t in tarefas}
    for t, antes in dependencias.items():
        for a in antes:
            seguintes[a].append(t)
    fila = deque(sorted(t for t, n in faltam.items() if n == 0))
    ordem = []
    while fila:
        t = fila.popleft()
        ordem.append(t)
        for s in sorted(seguintes[t]):
            faltam[s] -= 1
            if faltam[s] == 0:
                fila.append(s)
    if len(ordem) != len(tarefas):
        raise ValueError("há um ciclo nas dependências")
    return ordem

projeto = {"testes": {"código"}, "código": {"análise"},
           "deploy": {"testes", "documentação"},
           "documentação": {"análise"}}
print(" -> ".join(ordem_topologica(projeto)))
try:
    ordem_topologica({"a": {"b"}, "b": {"a"}})
except ValueError as e:
    print("Erro:", e)
