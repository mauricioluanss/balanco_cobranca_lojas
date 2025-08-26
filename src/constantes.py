from pathlib import Path

DIR_RAIZ = Path(__file__).parent
DIR_DATA = DIR_RAIZ / "data"

ARQ_CLIENTES = next((DIR_DATA / "clientes").glob("*"))
ARQ_PRODUTOS = next((DIR_DATA / "produtos").glob("*"))
ARQ_TIPOS = DIR_DATA / "tipos/tipos_e_valores.xlsx"
DIR_BASE = DIR_RAIZ / "output"
