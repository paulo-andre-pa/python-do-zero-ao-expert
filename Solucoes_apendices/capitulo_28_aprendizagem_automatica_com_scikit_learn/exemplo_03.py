# Capítulo 28 — Aprendizagem automática com scikit-learn
# Secção: Sobreajuste: decorar não é aprender

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier

profundidades = range(1, 16)
treino, teste = [], []
for p in profundidades:
    arvore = DecisionTreeClassifier(max_depth=p, random_state=0)
    arvore.fit(X_tr, y_tr)
    treino.append(arvore.score(X_tr, y_tr))
    teste.append(arvore.score(X_te, y_te))

fig, ax = plt.subplots(figsize=(7, 2.8))
ax.plot(profundidades, treino, "-o", color="0.6", label="treino")
ax.plot(profundidades, teste, "-s", color="0.1", label="teste")
ax.set_xlabel("profundidade máxima da árvore")
ax.set_ylabel("exatidão")
ax.spines[["top", "right"]].set_visible(False)
ax.legend(frameon=False)
fig.tight_layout()
