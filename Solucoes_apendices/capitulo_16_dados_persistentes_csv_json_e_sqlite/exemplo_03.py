# Capítulo 16 — Dados persistentes: CSV, JSON e SQLite
# Secção: JSON

import json

config = {
    "aplicacao": "Gestor de Stock",
    "versao": "2.1",
    "base_dados": {"caminho": "stock.db", "timeout": 5},
    "idiomas": ["pt", "en", "fr"],
    "modo_debug": False,
    "proxy": None,
}
texto = json.dumps(config, indent=2, ensure_ascii=False)
print(texto)

with open("config.json", "w", encoding="utf-8") as f:
    json.dump(config, f, indent=2, ensure_ascii=False)
with open("config.json", encoding="utf-8") as f:
    lido = json.load(f)
print(lido == config, lido["base_dados"]["timeout"])
