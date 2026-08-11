# O terceiro Scriopt é necessário para fazer uma análise visual inicial do conteúdo das abas, 
# mostrando as primeiras 8 linhas de cada uma. 
# Isso ajuda a entender como os dados realmente estão organizados antes de definir o tratamento.
# Algumas colunas estão nulas e com 'head' no local errado.

from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_SOURCE = BASE_DIR / "data_source"


def analisar_arquivo(nome_arquivo):
    caminho = DATA_SOURCE / nome_arquivo

    print("\n" + "=" * 80)
    print(f"ANÁLISE: {nome_arquivo}")
    print("=" * 80)

     # Abre o arquivo Excel com o Pandas.
    # Permite acessar as abas existentes no arquivo.
    excel = pd.ExcelFile(caminho)
 # Percorre todas as abas existentes no arquivo Excel.
    for aba in excel.sheet_names:
        df = pd.read_excel(caminho, sheet_name=aba, header=None)
        # Lê a aba atual e armazena os dados em um DataFrame.
        # header=None informa ao Pandas para NÃO considerar a primeira linha como nome das colunas.
        # Isso é importante para visualizar a estrutura original da planilha.

        print(f"\nAba: {aba}")
        print(f"Dimensões: {df.shape[0]:,} linhas x {df.shape[1]} colunas")
        # Exibe as dimensões da aba. 
        # df.shape[0] = quantidade de linhas. // df.shape[1] = quantidade de colunas.        

        print("\nPrimeiras 8 linhas:")
        print(df.head(8).to_string(index=False, header=False))
        # head(8) seleciona as primeiras 8 linhas.
        # to_string() transforma o DataFrame em texto para exibição no terminal.
        # index=False remove os números dos índices. // header=False evita exibir nomes de colunas.        

# Essa função em especial é utilizada para os arquivos que estão com o head 'null'
# Conforme visto em "inspecionar_estrutura.py"
def main():
    analisar_arquivo("Cadastro Clientes.xlsx")
    analisar_arquivo("Cadastro Lojas.xlsx")
 # Envia o arquivo Cadastro Lojas e Clientes.xlsx para análise.
     


if __name__ == "__main__":
    main()