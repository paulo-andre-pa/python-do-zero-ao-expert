# Projeto 6 — Triagem inteligente de pedidos de suporte
# Secção: Utilização

import numpy as np

probs = m.predict_proba(X_te)
confianca = probs.max(axis=1)
acerto = m.classes_[probs.argmax(axis=1)] == np.array(y_te)
print(f"{'limiar':>7}{'automáticos':>13}{'exatidão (automáticos)':>25}")
for limiar in (0.4, 0.5, 0.6, 0.7, 0.8, 0.9):
    auto = confianca >= limiar
    print(f"{limiar:>7.1f}{auto.mean():>13.1%}{acerto[auto].mean():>25.1%}")
