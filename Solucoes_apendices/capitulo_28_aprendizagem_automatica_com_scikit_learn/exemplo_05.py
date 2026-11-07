# Capítulo 28 — Aprendizagem automática com scikit-learn
# Secção: Pré-processamento com pipelines

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

rng = np.random.default_rng(1)
n = 1500
clientes = pd.DataFrame({
    "meses_cliente": rng.integers(1, 72, n),
    "fatura_mensal": rng.normal(35, 12, n).round(2),
    "reclamacoes": rng.poisson(0.6, n),
    "plano": rng.choice(["básico", "família", "empresa"], n),
    "pagamento": rng.choice(["débito", "cartão", "transferência"], n),
})
clientes.loc[rng.choice(n, 60), "fatura_mensal"] = np.nan  # em falta
risco = (-0.04 * clientes["meses_cliente"] + 0.9 * clientes["reclamacoes"]
         + 0.6 * (clientes["plano"] == "básico")
         + 0.5 * (clientes["pagamento"] == "transferência"))
clientes["cancelou"] = (risco + rng.normal(0, 0.8, n) > 0).astype(int)

numericas = ["meses_cliente", "fatura_mensal", "reclamacoes"]
categoricas = ["plano", "pagamento"]
preparacao = ColumnTransformer([
    ("num", Pipeline([("imputar", SimpleImputer(strategy="median")),
                      ("escalar", StandardScaler())]), numericas),
    ("cat", OneHotEncoder(handle_unknown="ignore"), categoricas),
])
modelo_churn = Pipeline([("prep", preparacao),
                         ("clf", LogisticRegression(max_iter=1000))])

X_c, y_c = clientes.drop(columns="cancelou"), clientes["cancelou"]
Xc_tr, Xc_te, yc_tr, yc_te = train_test_split(X_c, y_c, test_size=0.25,
                                              random_state=0, stratify=y_c)
modelo_churn.fit(Xc_tr, yc_tr)
print("taxa de cancelamento:", round(y_c.mean(), 3))
print("exatidão no teste:", round(modelo_churn.score(Xc_te, yc_te), 3))

nomes = modelo_churn["prep"].get_feature_names_out()
pesos = pd.Series(modelo_churn["clf"].coef_[0], index=nomes).sort_values()
print(pesos.round(2).to_string())
