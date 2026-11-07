# Capítulo 28 — Aprendizagem automática com scikit-learn
# Secção: Guardar e usar um modelo em produção

import joblib

joblib.dump(modelo_churn, "modelo_churn.joblib")
carregado = joblib.load("modelo_churn.joblib")
novo = pd.DataFrame([{"meses_cliente": 30, "fatura_mensal": 29.9,
                      "reclamacoes": 1, "plano": "básico",
                      "pagamento": "cartão"}])
print("probabilidade de cancelar:",
      round(carregado.predict_proba(novo)[0, 1], 2))
