# Capítulo 10 — Módulos, pacotes e ambientes virtuais
# Secção: Formas de importar

import conversores                      # importa o módulo
from conversores import milhas_para_km  # importa um nome
from conversores import celsius_para_fahrenheit as c2f   # com alias
import conversores as conv              # módulo com alias

print(milhas_para_km(10), c2f(0), conv.KM_POR_MILHA)
