import pandas as pd

from caminhos import ARQ_SPA, DIR_OUTPUT


def faz_conferencia_com_spa():
    df_tabela_dinamica = pd.read_excel(DIR_OUTPUT / "tabela_dinamica.xlsx")

    ABA = "Lojas com SPA"
    df_spa = pd.read_excel(ARQ_SPA, sheet_name=ABA)
    df_spa["CNPJ"] = df_spa["CNPJ"].str.strip()

    df_spa = df_spa.merge(
        df_tabela_dinamica[["CNPJ", "LOJA", "TOTAL PDV", "TOTAL GERAL"]],
        left_on="CNPJ",
        right_on="CNPJ",
        how="left",
    )

    df_spa.to_excel(DIR_OUTPUT / "conferencia_spa.xlsx", index=False)
