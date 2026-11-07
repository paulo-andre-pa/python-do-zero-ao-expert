# Apêndice B — Soluções de exercícios selecionados
# Secção: Capítulo 28 — Aprendizagem automática

from sklearn.datasets import load_breast_cancer
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import recall_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

X, y = load_breast_cancer(return_X_y=True)
X_tr, X_te, y_tr, y_te = train_test_split(X, y, random_state=0, stratify=y)
trivial = DummyClassifier(strategy="most_frequent")
logistica = make_pipeline(StandardScaler(),
                          LogisticRegression(max_iter=1000))
modelos = [("sempre 'benigno'", trivial),
           ("regressão logística", logistica)]
for nome, m in modelos:
    m.fit(X_tr, y_tr)
    p = m.predict(X_te)
    detetados = recall_score(y_te, p, pos_label=0)
    print(f"{nome:<20} exatidão={m.score(X_te, y_te):.3f}  "
          f"malignos detetados={detetados:.0%}")
