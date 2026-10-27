"""Uso: python -m pipeline.run <indicador> <etapa>"""
import argparse
import importlib

ETAPAS = ("coletar", "inspecionar", "limpar")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("indicador", help="nome do módulo em pipeline/indicadores")
    parser.add_argument("etapa", choices=ETAPAS)
    args = parser.parse_args()

    modulo = importlib.import_module(f"pipeline.indicadores.{args.indicador}")
    getattr(modulo, args.etapa)()


if __name__ == "__main__":
    main()
