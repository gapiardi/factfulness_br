"""Contrato do formato pronto (tidy), comum a todos os indicadores."""
import pandas as pd

COLUNAS = [
    "indicador",
    "ano",
    "valor",
    "unidade",
    "nivel",               # BR | UF
    "cod_territorio",      # código IBGE (1 = Brasil, 11..53 = UFs)
    "territorio",
    "sexo",                # total | homens | mulheres
    "categoria",           # ex.: rede_geral, poco; "total" quando não se aplica
    "tipo_valor",          # observado | estimativa | projecao
    "serie_metodologica",  # trecho comparável; muda a cada quebra
    "fonte_id",            # chave em metadados/<indicador>.yaml
]

NIVEIS = {"BR", "UF"}
SEXOS = {"total", "homens", "mulheres"}
TIPOS_VALOR = {"observado", "estimativa", "projecao"}


def validar_schema(df: pd.DataFrame) -> None:
    faltando = set(COLUNAS) - set(df.columns)
    if faltando:
        raise ValueError(f"Colunas ausentes: {sorted(faltando)}")

    for coluna, permitidos in (("nivel", NIVEIS), ("sexo", SEXOS), ("tipo_valor", TIPOS_VALOR)):
        invalidos = set(df[coluna].unique()) - permitidos
        if invalidos:
            raise ValueError(f"Valores inválidos em {coluna}: {sorted(invalidos)}")

    chave = ["indicador", "ano", "cod_territorio", "sexo", "categoria", "serie_metodologica"]
    duplicadas = df.duplicated(chave)
    if duplicadas.any():
        raise ValueError(f"{duplicadas.sum()} linhas duplicadas na chave {chave}")

    if df["valor"].isna().any():
        raise ValueError("Há valores nulos; lacunas devem ser omitidas e documentadas, não gravadas como NaN.")
