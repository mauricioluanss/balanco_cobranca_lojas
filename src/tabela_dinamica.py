import pandas as pd

from caminhos import COLUNAS_TIPOS, DIR_OUTPUT


def cria_tabela_dinamica():
    df_produtos = pd.read_excel(DIR_OUTPUT / "tabela_base.xlsx")

    tabela_dinamica = df_produtos.pivot_table(
        index="CNPJ",
        columns=COLUNAS_TIPOS["COL_TIPO"],
        values=COLUNAS_TIPOS["COL_VALOR"],
        aggfunc="sum",
    )

    # soma o total de PDV
    colunas_total_pdv = ["OUTROS", "PDV", "PIX"]
    total_pdv = tabela_dinamica[colunas_total_pdv].sum(axis=1)
    tabela_dinamica["TOTAL PDV"] = total_pdv

    # soma o total geral
    colunas_total_geral = ["LOJA", "TOTAL PDV"]
    total_geral = tabela_dinamica[colunas_total_geral].sum(axis=1)
    tabela_dinamica["TOTAL GERAL"] = total_geral

    tabela_dinamica.to_excel((DIR_OUTPUT / "tabela_dinamica.xlsx"))
    print(tabela_dinamica)
