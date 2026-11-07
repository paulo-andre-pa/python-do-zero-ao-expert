# Capítulo 28 — Aprendizagem automática com scikit-learn
# Secção: Avaliar um classificador

from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

dados = load_breast_cancer()
X, y = dados.data, dados.target            # 0 = maligno, 1 = benigno
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.25,
                                          random_state=0, stratify=y)
clf = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000))
clf.fit(X_tr, y_tr)
previsto = clf.predict(X_te)
print(confusion_matrix(y_te, previsto))
print(classification_report(y_te, previsto,
                            target_names=["maligno", "benigno"], digits=3))
