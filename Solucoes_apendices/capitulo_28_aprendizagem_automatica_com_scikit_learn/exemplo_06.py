# Capítulo 28 — Aprendizagem automática com scikit-learn
# Secção: Regressão: prever números

from sklearn.datasets import load_diabetes
from sklearn.dummy import DummyRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error, r2_score

X, y = load_diabetes(return_X_y=True)
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.25,
                                          random_state=0)
modelos = {"referência (média)": DummyRegressor(),
           "Ridge (linear)": Ridge(alpha=1.0),
           "floresta aleatória": RandomForestRegressor(n_estimators=300,
                                                       random_state=0)}
for nome, m in modelos.items():
    m.fit(X_tr, y_tr)
    p = m.predict(X_te)
    print(f"{nome:<20} MAE={mean_absolute_error(y_te, p):6.1f}  "
          f"R²={r2_score(y_te, p):6.3f}")
