# O Segundo Script é responsável por inspecionar a estrutura dos arquivos Excel, sem alterar os dados.
# Ele identifica os arquivos, lista as abas e mostra a quantidade de linhas, colunas e os nomes
# das colunas de cada aba.
# Antes de aplicar o tratamento nos dados. Isso é especialmente útil no seu projeto porque 
# permite descobrir exatamente quais abas e colunas existem antes de definir.

from pathlib import Path
import pandas as pd
# Preciso utilizar o Pandas para ler e analisar os arquivos Excel.

# Preciso definir a raiz do caminho e definir novamente o diretório onde estão os arquivos originais ( não versionados )
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_SOURCE = BASE_DIR / "data_source"

def main():
    arquivos = list(DATA_SOURCE.glob("*.xlsx"))

    if not arquivos:
        print("Nenhum arquivo .xlsx encontrado.")
        return

    print(f"\nArquivos encontrados: {len(arquivos)}\n")

    for arquivo in arquivos:
        print("=" * 70)
        print(f"ARQUIVO: {arquivo.name}")
        print("=" * 70)

        excel = pd.ExcelFile(arquivo)
# Abre o arquivo Excel utilizando o Pandas.
# Permite identificar as abas existentes no arquivo.        

        print(f"Abas: {excel.sheet_names}\n")
# Exibe os nomes de todas as abas existentes no Excel.        

  # Percorre cada aba encontrada no arquivo.
        for aba in excel.sheet_names:
            df = pd.read_excel(arquivo, sheet_name=aba)
            # Lê a aba atual do Excel.
            # O resultado é armazenado na variável 'df' ( padrão Pandas )

            print(f"  Aba: {aba}")
            print(f"  Linhas: {len(df):,}")
            print(f"  Colunas: {len(df.columns)}")
            print("  Colunas:")
 # Percorre cada coluna existente no DataFrame.
            for coluna in df.columns:
                print(f"    - {coluna}")

            print()

if __name__ == "__main__":
    main()