import pandas as pd

from pipeline.config import carregar_metadados, dir_brutos
from pipeline.fontes.arquivo import baixar

ID = "expectativa_vida"


def coletar() -> None:
    for fonte in carregar_metadados(ID)["fontes"]:
        registro = baixar(fonte["url_arquivo"], dir_brutos(ID) / fonte["arquivo"])
        print(f"{registro['arquivo']}: {registro['bytes']:,} bytes, sha256 {registro['sha256'][:12]}")


def inspecionar(linhas: int = 15) -> None:
    """Mostra abas e cabeçalhos da planilha bruta, para definir o parser de limpar()."""
    for fonte in carregar_metadados(ID)["fontes"]:
        planilhas = pd.read_excel(dir_brutos(ID) / fonte["arquivo"], sheet_name=None, header=None)
        for nome, df in planilhas.items():
            print(f"\n=== aba '{nome}': {df.shape[0]} linhas x {df.shape[1]} colunas ===")
            print(df.head(linhas).to_string())


def limpar() -> None:
    raise NotImplementedError("Aguardando a saída de inspecionar() para definir o parser.")
