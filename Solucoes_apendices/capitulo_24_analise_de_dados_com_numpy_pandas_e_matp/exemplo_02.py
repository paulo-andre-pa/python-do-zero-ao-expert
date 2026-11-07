# Capítulo 24 — Análise de dados com NumPy, pandas e Matplotlib
# Secção: NumPy: cálculo vetorizado

import time

valores = np.random.default_rng(42).uniform(0, 100, 1_000_000)
lista = valores.tolist()

t = time.perf_counter(); s1 = sum(v * v for v in lista)
t_py = time.perf_counter() - t
t = time.perf_counter(); s2 = (valores * valores).sum()
t_np = time.perf_counter() - t
print(f"Python: {t_py * 1000:.0f} ms | NumPy: {t_np * 1000:.1f} ms | "
      f"~{t_py / t_np:.0f}x")
