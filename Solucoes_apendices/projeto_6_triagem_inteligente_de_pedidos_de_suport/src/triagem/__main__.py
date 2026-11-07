"""Uso:  python -m triagem treinar modelo.joblib
        python -m triagem classificar modelo.joblib "texto do pedido" """
import sys
from pathlib import Path

from triagem import dados, modelo
from triagem.servico import Triagem

def main(argv: list[str]) -> int:
    comando, caminho = argv[0], Path(argv[1])
    if comando == "treinar":
        m, _, relatorio = modelo.treinar(*dados.gerar(4000))
        modelo.guardar(m, caminho)
        print(relatorio)
    elif comando == "classificar":
        d = Triagem(modelo.carregar(caminho)).classificar(argv[2])
        print(d)
    else:
        print(__doc__)
        return 1
    return 0

if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
