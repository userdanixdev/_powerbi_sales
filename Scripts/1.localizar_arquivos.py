# O primeiro script python do projeto tem como objetivo de localizar os arquivos xlsx existentes

from pathlib import Path


# Diretórios:
### Base_dir Define a raiz do projeto.
BASE_DIR = Path(__file__).resolve().parent.parent
# __file__ = caminho deste script. // # resolve() = transforma em caminho absoluto.
# parent = diretório onde o script está. // # parent.parent = sobe um nível adicional até a raiz do projeto.

DATA_SOURCE = BASE_DIR / "data_source"
# Define o diretório onde estão os arquivos Excel originais.
SAMPLE = BASE_DIR / "data" / "sample"
# Define o diretório onde serão armazenados os arquivos de amostra.

def main():
    SAMPLE.mkdir(parents=True, exist_ok = True)
 # Cria o diretório data/sample. // parents=True permite criar diretórios intermediários, se necessário.
 # exist_ok=True evita erro caso a pasta já exista.    
    arquivos = list(DATA_SOURCE.glob("*.xlsx"))
# Procura todos os arquivos com extensão .xlsx dentro de data_source.
# glob("*.xlsx") localiza os arquivos Excel. // list() transforma o resultado em uma lista.    
    print(f"Diretório das fontes: {DATA_SOURCE}")
    print(f" Arquivos encontrados: {len(arquivos)}")
    # Percorre cada arquivo encontrado.
    for arquivo in arquivos:
        print(f"Processando: {arquivo.name}")

if __name__== "__main__":
    main()

