# Capítulo 28 — Aprendizagem automática com scikit-learn
# Secção: Aprendizagem não supervisionada: segmentar clientes

from sklearn.cluster import KMeans

rng = np.random.default_rng(3)
gasto = np.concatenate([rng.normal(30, 8, 120), rng.normal(120, 20, 80),
                        rng.normal(70, 10, 100)])
frequencia = np.concatenate([rng.normal(2, 0.8, 120), rng.normal(3, 1, 80),
                             rng.normal(9, 1.5, 100)])
X_seg = StandardScaler().fit_transform(np.column_stack([gasto, frequencia]))
kmeans = KMeans(n_clusters=3, n_init=10, random_state=0).fit(X_seg)

segmentos = pd.DataFrame({"gasto": gasto, "frequencia": frequencia,
                          "grupo": kmeans.labels_})
resumo = segmentos.groupby("grupo").agg(
    clientes=("gasto", "size"), gasto_medio=("gasto", "mean"),
    visitas_mes=("frequencia", "mean"))
print(resumo.round(1))

fig, ax = plt.subplots(figsize=(7, 3))
for g, marca in zip(range(3), ["o", "s", "^"]):
    s = segmentos[segmentos["grupo"] == g]
    ax.scatter(s["gasto"], s["frequencia"], marker=marca, s=14,
               color=["0.15", "0.45", "0.7"][g], label=f"grupo {g}")
ax.set_xlabel("gasto médio por visita (€)")
ax.set_ylabel("visitas por mês")
ax.spines[["top", "right"]].set_visible(False)
ax.legend(frameon=False)
fig.tight_layout()
