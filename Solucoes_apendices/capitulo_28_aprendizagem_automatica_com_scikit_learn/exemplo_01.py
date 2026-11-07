# Capítulo 28 — Aprendizagem automática com scikit-learn
# Secção: O primeiro modelo

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

X, y = load_iris(return_X_y=True)
print(X.shape, y.shape, X[0], y[0])

X_treino, X_teste, y_treino, y_teste = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y)

modelo = KNeighborsClassifier(n_neighbors=5)
modelo.fit(X_treino, y_treino)
print("exatidão no teste:", round(modelo.score(X_teste, y_teste), 3))
nova_flor = [[6.1, 2.8, 4.7, 1.2]]
especie = load_iris().target_names[modelo.predict(nova_flor)[0]]
print("previsão para uma flor nova:", especie)
