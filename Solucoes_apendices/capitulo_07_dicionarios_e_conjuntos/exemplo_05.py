# Capítulo 7 — Dicionários e conjuntos
# Secção: Métodos essenciais

config = {"tema": "claro", "idioma": "pt"}
config.update({"idioma": "en", "notificacoes": True})   # junta
print(config)
valor = config.pop("tema")              # remove e devolve
print(valor, config)
config.setdefault("fonte", "Arial")     # só define se não existir
config.setdefault("idioma", "fr")       # já existe: não altera
print(config)
