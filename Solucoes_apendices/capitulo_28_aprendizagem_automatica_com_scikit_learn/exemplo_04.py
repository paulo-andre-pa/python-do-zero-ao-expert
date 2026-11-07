# Capítulo 28 — Aprendizagem automática com scikit-learn
# Secção: Validação cruzada e procura de hiperparâmetros

from sklearn.model_selection import GridSearchCV, cross_val_score
from sklearn.ensemble import RandomForestClassifier

notas = cross_val_score(clf, X_tr, y_tr, cv=5, scoring="f1")
print("F1 por partição:", notas.round(3), "média:", round(notas.mean(), 3))

procura = GridSearchCV(
    RandomForestClassifier(random_state=0),
    param_grid={"n_estimators": [50, 200], "max_depth": [3, 6, None]},
    cv=5, scoring="f1")
procura.fit(X_tr, y_tr)
print("melhores hiperparâmetros:", procura.best_params_)
print("F1 no teste:", round(procura.score(X_te, y_te), 3))
