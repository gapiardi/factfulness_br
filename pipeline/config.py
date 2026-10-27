from pathlib import Path

import yaml

RAIZ = Path(__file__).resolve().parents[1]
DIR_BRUTOS = RAIZ / "dados" / "brutos"
DIR_PRONTOS = RAIZ / "dados" / "prontos"
DIR_METADADOS = RAIZ / "metadados"
DIR_CONFERENCIA = RAIZ / "conferencia"


def dir_brutos(indicador: str) -> Path:
    return DIR_BRUTOS / indicador


def carregar_metadados(indicador: str) -> dict:
    with open(DIR_METADADOS / f"{indicador}.yaml", encoding="utf-8") as f:
        return yaml.safe_load(f)
