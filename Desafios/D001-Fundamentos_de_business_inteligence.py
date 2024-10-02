def identificar_termo_bi(termo):
    if termo == "ETL":
        return "Processo de extrair, transformar e carregar dados de diversas fontes."
    elif termo == "Data Warehousing":
        return "Armazenamento centralizado de dados para análise e relatórios."
    elif termo == "Dashboard":
        return "Ferramenta visual para monitoramento e análise de métricas."
    elif termo == "Data Mining":
        return "o processo de compreensão dos dados por meio da limpeza de dados brutos, da descoberta de padrões, da criação de modelos e do teste desses modelos."
    else:
        return "Termo não reconhecido"

entrada = input()


print(identificar_termo_bi(entrada))