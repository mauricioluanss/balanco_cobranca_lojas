from src.scripts import conferencia, tabela_base, tabela_dinamica


def main():
    tabela_base.cria_tabela_base()
    tabela_dinamica.cria_tabela_dinamica()
    conferencia.faz_conferencia_com_spa()


if __name__ == "__main__":
    main()
