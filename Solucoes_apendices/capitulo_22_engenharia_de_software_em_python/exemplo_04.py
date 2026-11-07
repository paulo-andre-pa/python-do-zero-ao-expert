# Capítulo 22 — Engenharia de software em Python
# Secção: Configuração e segredos

import tomllib

with open("config.toml", "rb") as f:          # tomllib exige modo binário
    config = tomllib.load(f)
print(config["aplicacao"]["nome"], config["base_dados"]["timeout"])
