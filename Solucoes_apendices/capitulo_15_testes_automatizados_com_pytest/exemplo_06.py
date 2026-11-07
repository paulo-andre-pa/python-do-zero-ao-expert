# Capítulo 15 — Testes automatizados com pytest
# Secção: Mocks: isolar dependências

import random
from unittest.mock import patch

def lancar_dado():
    return random.randint(1, 6)

with patch("random.randint", return_value=6):
    assert lancar_dado() == 6
print("depois do patch, volta ao normal:", 1 <= lancar_dado() <= 6)
