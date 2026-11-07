# Capítulo 7 — Dicionários e conjuntos
# Secção: Porque são tão rápidos?

from collections import Counter

linhas = [
    "10.0.0.5 GET /index.html 200",
    "10.0.0.8 GET /produtos 200",
    "10.0.0.5 POST /login 302",
    "10.0.0.9 GET /admin 404",
    "10.0.0.5 GET /carrinho 200",
    "10.0.0.8 GET /wp-login.php 404",
    "10.0.0.9 GET /admin 404",
    "10.0.0.5 GET /checkout 500",
]
registos = [l.split() for l in linhas]
por_ip = Counter(ip for ip, *_ in registos)
erros_404 = {caminho for _, _, caminho, cod in registos if cod == "404"}
sucesso = sum(1 for *_, cod in registos if cod.startswith("2"))
print("Mais ativos:", por_ip.most_common(2))
print("Caminhos 404:", sorted(erros_404))
print(f"Sucesso: {sucesso / len(registos):.0%}")
