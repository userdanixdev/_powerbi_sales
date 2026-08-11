# Diferentemente dos três anteriores, ele não serve apenas para inspecionar os arquivos:
# ele lê as bases, seleciona as colunas relevantes, limita a quantidade de registros e salva 
# uma cópia reduzida em data/sample.
# Obs: Esse script é uma amostra reduzida e estruturada dos dados, não necessariamente uma base anonimizada.

from pathlib import Path
import pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_SOURCE = BASE_DIR / "data_source"
SAMPLE = BASE_DIR / "data" / "sample"

QTD_LINHAS = 10
# Define a quantidade de linhas que serão mantidas em cada sample.

def main():

    SAMPLE.mkdir(parents=True, exist_ok=True)

    arquivos = list(DATA_SOURCE.glob("*.xlsx"))

    print(f"Arquivos encontrados: {len(arquivos)}")
 # Percorre cada arquivo encontrado.
    for arquivo in arquivos:

        print(f"Gerando sample: {arquivo.name}")

        if arquivo.name == "Cadastro Clientes.xlsx":
            # Lê a aba Plan1 do arquivo // skiprows=2 ignora as duas primeiras linhas da planilha.
            # Conforme visto nos scripts anteriores
            df = pd.read_excel(
                arquivo,
                sheet_name="Plan1",
                skiprows=2
            )
 # Mantém somente as colunas selecionadas do cadastro de clientes para amostra.
            df = df[
                [
                    "ID Cliente",
                    "Genero",
                    "Estado Civil",
                    "Num Filhos",
                    "Nivel Escolar"
                ]
            ]
# Verifica se o nome do arquivo começa com "Base Vendas".
# Isso permite tratar diferentes arquivos de vendas com o mesmo padrão.
        elif arquivo.name.startswith("Base Vendas"):

            df = pd.read_excel(
                arquivo,
                sheet_name="Plan1"
            )

            df = df[
                [
                    "Data da Venda",
                    "ID Cliente",
                    "Qtd Vendida",
                    "ID Loja"
                ]
            ]
# Mantém somente as colunas necessárias da base de vendas para amostra.
        elif arquivo.name == "Cadastro Lojas.xlsx":

            df = pd.read_excel(
                arquivo,
                sheet_name="Plan1"
            )

            df = df[
                [
                    "ID Loja",
                    "Quantidade Colaboradores",
                    "Tipo",
                    "id Localidade"
                ]
            ]
 # Mantém somente as colunas selecionadas do cadastro de lojas para amostra.
        elif arquivo.name == "Cadastro Produtos.xlsx":

            df = pd.read_excel(
                arquivo,
                sheet_name="Produtos"
            )

            df = df[
                [
                    "Produto",
                    "Marca",
                    "Tipo do Produto",
                    "Preço Unitario",
                    "Custo Unitario"
                ]
            ]

        else:

            df = pd.read_excel(
                arquivo,
                sheet_name="Plan1"
            )
# Mantém somente as primeiras 10 linhas do DataFrame. // A quantidade é definida pela variável QTD_LINHAS.
        df = df.head(QTD_LINHAS)
# Define o nome da aba que será criada no arquivo de saída.
# Para Cadastro Produtos.xlsx utiliza "Produtos". // Para os demais arquivos utiliza "Plan1".
        aba = "Produtos" if arquivo.name == "Cadastro Produtos.xlsx" else "Plan1"

# Salva o DataFrame como um novo arquivo Excel dentro de data/sample.
# Mantém o mesmo nome do arquivo original.
# index=False evita salvar o índice do DataFrame como uma coluna.
# sheet_name define o nome da aba do arquivo gerado.
        df.to_excel(
            SAMPLE / arquivo.name,
            index=False,
            sheet_name=aba
        )

    print("\nSample gerado com sucesso!")
    print(f"Diretório: {SAMPLE}")


if __name__ == "__main__":
    main()