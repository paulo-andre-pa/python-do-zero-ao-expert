# Capítulo 10 — Módulos, pacotes e ambientes virtuais
# Secção: O idioma `__name__ == "__main__"`

import estatistica      # não mostra nada: main() não é executada
print(estatistica.mediana([5, 1, 3, 2]))
