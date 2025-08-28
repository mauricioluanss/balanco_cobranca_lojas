from pathlib import Path

# diretorios
DIR_RAIZ = Path(__file__).parent
DIR_DATA = DIR_RAIZ / "data"
DIR_OUTPUT = DIR_RAIZ / "output"

# arquivos
ARQ_CLIENTES = next((DIR_DATA / "clientes").glob("*"))
ARQ_PRODUTOS = next((DIR_DATA / "produtos").glob("*"))
ARQ_SPA = next((DIR_DATA / "spa").glob("*"))
ARQ_TIPOS = DIR_DATA / "tipos/tipos_e_valores.xlsx"

# mapa das colunas para os arquivos de input
COLUNAS_PRODUTOS = {
    "COL_CLIENTE": "Cliente",
    "COL_PRODUTO_SERVICO": "Produto/Serviço",
    "COL_QUANTIDADE": "Quantidade",
}
COLUNAS_CLIENTES = {
    "COL_FANTASIA": "Nome",
    "COL_RAZAO_SOCIAL": "Razão Social",
    "COL_CNPJ": "CNPJ",
}
COLUNAS_TIPOS = {
    "COL_PRODUTO_SERVICO": "PRODUTOS/SERVICO",
    "COL_TIPO": "TIPO",
    "COL_VALOR": "VALOR",
}
