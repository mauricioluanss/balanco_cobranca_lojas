import pandas as pd

from caminhos import (
    ARQ_CLIENTES,
    ARQ_PRODUTOS,
    ARQ_TIPOS,
    COLUNAS_CLIENTES,
    COLUNAS_PRODUTOS,
    COLUNAS_TIPOS,
    DIR_OUTPUT,
)


def cria_tabela_base():
    # 1 - Carrega os arquivos de entrada e faz a limpeza das colunas.
    df_produtos = pd.read_csv(ARQ_PRODUTOS, usecols=list(COLUNAS_PRODUTOS.values()))
    df_produtos.columns = df_produtos.columns.str.strip()
    df_produtos[COLUNAS_PRODUTOS["COL_QUANTIDADE"]] = pd.to_numeric(
        df_produtos[COLUNAS_PRODUTOS["COL_QUANTIDADE"]], errors="coerce"
    )

    df_clientes = pd.read_excel(ARQ_CLIENTES, usecols=list(COLUNAS_CLIENTES.values()))
    df_clientes.columns = df_clientes.columns.str.strip()

    df_tipos_valores = pd.read_excel(ARQ_TIPOS)
    df_tipos_valores.columns = df_tipos_valores.columns.str.strip()
    df_tipos_valores[COLUNAS_TIPOS["COL_VALOR"]] = pd.to_numeric(
        df_tipos_valores[COLUNAS_TIPOS["COL_VALOR"]], errors="coerce"
    )

    # 2 - Realiza o merge de dados entre produtos e clientes, buscando o CNPJ correspondente e depois
    # entre produtos e tipos/valores, buscando o tipo e valor correspondente.
    df_produtos = df_produtos.merge(
        df_clientes[[COLUNAS_CLIENTES["COL_FANTASIA"], COLUNAS_CLIENTES["COL_CNPJ"]]],
        left_on=COLUNAS_PRODUTOS["COL_CLIENTE"],
        right_on=COLUNAS_CLIENTES["COL_FANTASIA"],
        how="left",
    )

    df_produtos = df_produtos.merge(
        df_tipos_valores,
        left_on=COLUNAS_PRODUTOS["COL_PRODUTO_SERVICO"],
        right_on=COLUNAS_TIPOS["COL_PRODUTO_SERVICO"],
        how="left",
    )

    df_produtos = df_produtos.drop(
        columns=[COLUNAS_CLIENTES["COL_FANTASIA"], COLUNAS_TIPOS["COL_PRODUTO_SERVICO"]]
    )
    df_produtos.to_excel((DIR_OUTPUT / "tabela_base.xlsx"), index=False)
    print(df_produtos)
