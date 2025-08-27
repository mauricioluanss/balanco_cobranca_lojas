from conferencia import faz_conferencia_com_spa
from main import cria_tabela_base
from tabela_dinamica import cria_tabela_dinamica


def main():
    cria_tabela_base()
    cria_tabela_dinamica()
    faz_conferencia_com_spa()


main()
