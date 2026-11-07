# Capítulo 7 — Dicionários e conjuntos
# Secção: Contar e agrupar

from collections import Counter

votos = ["A", "B", "A", "C", "A", "B", "A"]
c = Counter(votos)
print(c)
print(c.most_common(2))
print(Counter("mississippi").most_common(3))
