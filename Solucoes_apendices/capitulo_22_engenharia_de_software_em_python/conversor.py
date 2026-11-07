"""Converte valores entre moedas."""
import argparse

TAXAS = {"EUR": 1.0, "USD": 1.08, "AOA": 980.0, "BRL": 5.9}

def criar_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="conversor", description="Converte valores entre moedas.")
    p.add_argument("valor", type=float, help="montante a converter")
    p.add_argument("origem", choices=TAXAS, help="moeda de origem")
    p.add_argument("destino", choices=TAXAS, help="moeda de destino")
    p.add_argument("-c", "--casas", type=int, default=2,
                   help="casas decimais (omissão: 2)")
    p.add_argument("-v", "--verboso", action="store_true",
                   help="mostra a taxa usada")
    return p

def main(argv=None) -> int:
    args = criar_parser().parse_args(argv)
    taxa = TAXAS[args.destino] / TAXAS[args.origem]
    if args.verboso:
        print(f"taxa {args.origem}->{args.destino}: {taxa:.4f}")
    print(f"{args.valor * taxa:.{args.casas}f} {args.destino}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
