# 📊 Análise de Vendas e Performance Comercial

> Projeto de Business Intelligence desenvolvido com Power BI para transformar dados operacionais de vendas, devoluções e clientes em informações para suporte à tomada de decisão.

---

## 📌 Sobre o projeto

Este projeto simula um cenário de uma empresa varejista que possui uma operação comercial consolidada, mas ainda depende de diferentes arquivos Excel para armazenar informações relacionadas às suas vendas, clientes e devoluções.

Ao longo dos anos, a empresa acumulou dados de vendas referentes aos períodos de **2020, 2021 e 2022**, além de informações cadastrais de clientes e registros de devoluções.

Embora os dados estejam disponíveis, a ausência de uma visão analítica centralizada dificulta a identificação de tendências, oportunidades comerciais e problemas operacionais.

O objetivo deste projeto é desenvolver uma solução de **Business Intelligence utilizando Power BI**, permitindo transformar os dados existentes em indicadores e visualizações que apoiem a gestão comercial.

---

## 🏢 Cenário empresarial

Para este estudo de caso, considera-se uma empresa fictícia chamada **NovaComercial**, uma empresa varejista que comercializa produtos para consumidores de diferentes regiões.

A área comercial possui dados históricos de suas operações, porém as informações são mantidas em arquivos separados.

Atualmente, a gestão precisa consultar diferentes planilhas para responder perguntas simples como:

* Quanto a empresa vendeu em determinado período?
* Como as vendas evoluíram ao longo dos anos?
* Quais produtos apresentam melhor desempenho?
* Quais clientes possuem maior participação nas vendas?
* Quais regiões apresentam melhor desempenho comercial?
* Qual é o impacto das devoluções sobre as vendas?
* Em quais períodos houve crescimento ou queda nas vendas?
* Quais segmentos da operação precisam de maior atenção?

---

# ❗ Problema de negócio

A empresa possui um volume relevante de informações comerciais, mas os dados estão distribuídos em diferentes arquivos e períodos.

A inexistência de uma visão consolidada gera alguns problemas:

### 1. Dados descentralizados

As informações de vendas estão separadas por período, enquanto os dados de clientes e devoluções estão armazenados em outras fontes.

Isso dificulta a análise integrada da operação.

### 2. Baixa visibilidade da performance

A gestão não possui uma visão única para acompanhar indicadores comerciais e identificar rapidamente alterações no desempenho.

### 3. Dificuldade para identificar tendências

Sem uma análise histórica estruturada, torna-se mais difícil compreender:

* evolução das vendas;
* sazonalidade;
* períodos de crescimento;
* períodos de queda;
* comportamento dos clientes;
* desempenho dos produtos.

### 4. Impacto das devoluções

Analisar apenas o volume vendido pode gerar uma visão incompleta da operação.

As devoluções precisam ser analisadas em conjunto com as vendas para identificar possíveis impactos no resultado comercial.

### 5. Dependência de análises manuais

A consolidação de informações em planilhas aumenta o esforço operacional e dificulta a atualização dos indicadores.

---

# 🎯 Objetivo da solução

Desenvolver um **Dashboard de Vendas em Power BI** capaz de consolidar os dados comerciais da empresa e disponibilizar uma visão analítica para acompanhamento da operação.

A solução busca transformar dados brutos em informações úteis para diferentes níveis de decisão:

**Dados → Tratamento → Modelo de dados → Indicadores → Visualização → Decisão**

---

# 💡 Solução proposta

A solução utiliza o **Power BI** como camada de análise e visualização.

Os dados provenientes dos arquivos Excel são tratados e organizados para formar um modelo analítico capaz de relacionar diferentes aspectos da operação comercial.

### Fluxo da solução

```text
                 ┌─────────────────────┐
                 │   Arquivos Excel    │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │   Power Query / M   │
                 │ Tratamento dos dados│
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │    Modelo de dados  │
                 │       Power BI      │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │         DAX         │
                 │     Indicadores     │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │ Dashboard de Vendas │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │  Tomada de decisão  │
                 └─────────────────────┘
```

---

# 📂 Fontes de dados

O projeto inicial utiliza diferentes arquivos para representar as principais fontes de informação da operação.

| Fonte                     | Descrição                           |
| ------------------------- | ----------------------------------- |
| `Base Vendas - 2020.xlsx` | Dados de vendas do ano de 2020      |
| `Base Vendas - 2021.xlsx` | Dados de vendas do ano de 2021      |
| `Base Vendas - 2022.xlsx` | Dados de vendas do ano de 2022      |
| `Base Devoluções.xlsx`    | Registros de devoluções             |
| `Cadastro Clientes.xlsx`  | Informações cadastrais dos clientes |
| `Cadastro Localidades.xlsx`  | Informações cadastrais dos clientes |
| `Cadastro Lojas.xlsx`  | Informações cadastrais dos clientes |
| `Cadastro Produtos.xlsx`  | Informações cadastrais dos clientes |

> **Importante:** os arquivos contendo dados de clientes e outras informações potencialmente sensíveis não devem ser disponibilizados publicamente no repositório. Para publicação no GitHub, devem ser utilizados dados anonimizados, dados sintéticos ou apenas estruturas/amostras sem informações pessoais.

---

## 🔐 Segurança e Proteção de Dados

As fontes originais utilizadas durante o desenvolvimento não são disponibilizadas no repositório, pois podem conter informações pessoais e dados que não devem ser publicados.

Entre os campos identificados nas fontes originais estão informações como:

- Nome;
- Sobrenome;
- E-mail;
- Data de nascimento;
- Documento;
- Nome de gerente;
- Documento de gerente.

> Essas informações são mantidas fora do repositório público.

## Sample

Para permitir que outras pessoas compreendam a estrutura dos dados sem expor informações pessoais, foi criada uma versão reduzida das bases em:

```data/sample/```

O sample utiliza os próprios dados de origem, porém com:

- quantidade reduzida de registros;
- remoção de campos de identificação pessoal;
- manutenção das principais informações necessárias para demonstrar a estrutura das bases.

A geração do sample é realizada por um script Python separado.

```
data/
├── data_source/
│   └── arquivos originais
│
└── sample/
    └── arquivos reduzidos para demonstração
```

***Os arquivos originais permanecem no ambiente local e não devem ser versionados no Git.***

# 🔄 Tratamento dos dados

Antes da construção dos indicadores, os dados passam por processos de preparação e padronização.

Entre as etapas consideradas estão:

* importação das fontes;
* padronização de nomes e tipos de dados;
* tratamento de valores nulos;
* correção de inconsistências;
* padronização de campos;
* combinação das bases históricas;
* relacionamento entre entidades;
* criação de campos auxiliares;
* preparação dos dados para análise.

> O objetivo é garantir que o modelo utilizado pelo Power BI possua dados consistentes e adequados para análise.

---

# 📈 Indicadores

O dashboard foi desenvolvido para permitir o acompanhamento de indicadores comerciais e análises históricas.

Entre as principais análises estão:

* faturamento;
* quantidade de vendas;
* evolução das vendas;
* desempenho por período;
* desempenho por produto;
* desempenho por cliente;
* análise de devoluções;
* participação relativa nas vendas;
* comparação entre períodos;
* identificação de melhores e piores desempenhos.

Os indicadores são calculados utilizando **medidas DAX**, permitindo que os resultados sejam atualizados dinamicamente conforme os filtros aplicados no relatório.

---

# 🔎 Perguntas de negócio respondidas

A solução foi construída para responder perguntas como:

### Performance comercial

> Qual foi o desempenho das vendas ao longo do período analisado?

### Evolução temporal

> Como as vendas se comportaram entre 2020, 2021 e 2022?

### Produtos

> Quais produtos apresentam maior participação nas vendas?

### Clientes

> Quais clientes possuem maior representatividade no resultado comercial?

### Devoluções

> Como as devoluções se distribuem ao longo do período?

### Gestão

> Quais áreas da operação apresentam oportunidades de melhoria?

---

# 📊 Dashboard

O resultado final é um **Dashboard de Vendas desenvolvido no Power BI**, permitindo que o usuário explore os dados de maneira interativa por meio de filtros e diferentes visualizações.

A proposta é substituir análises manuais e fragmentadas por uma visão centralizada da operação.

### Principais características

* filtros interativos;
* indicadores de desempenho;
* análises temporais;
* visualizações comerciais;
* análise de devoluções;
* navegação dinâmica;
* visão consolidada dos dados.

---

## 🛠️ Tecnologias utilizadas

## Dados e Preparação:

* **Python**
* **Pandas**
* **OpenPyXL**
* **Excel**

## Análise e Visualização:

* **Power BI**
* **Power Query**
* **DAX**

## Versionamento:

* **Git**
* **GitHub**

---

## 📂 Estrutura do Projeto
```text
project_powerbi_sales/
│
├── data/
│   ├── data_source/
│   │     └── arquivos originais
│   │
│   └── sample/
│         └── arquivos para demonstração
│
├── Scripts/
│   ├── 1.localizar_arquivos.py
│   ├── 2.inspecionar_estrutura.py
│   ├── 3.analisar_conteudo.py
│   └── generate_sample.py
│
├── PowerBI/
│      └── relatório Power BI
│
├── .gitignore
└── README.md
```

> Os dados originais contendo informações pessoais ou potencialmente sensíveis não fazem parte do repositório público.

---

## 🔐 Privacidade e proteção de dados

O projeto foi estruturado considerando a necessidade de evitar a exposição de informações pessoais.

A base de clientes utilizada no desenvolvimento possui informações cadastrais que podem incluir dados pessoais. Portanto, esses arquivos **não devem ser versionados em um repositório público**.

Para fins de portfólio, a publicação deve utilizar:

* dados anonimizados;
* dados sintéticos;
* amostras sem informações pessoais; ou
* somente a estrutura necessária para reproduzir o projeto.

O objetivo é demonstrar as técnicas utilizadas sem expor informações de clientes.

---

# 🚀 Resultado esperado

A implementação da solução permite transformar uma operação baseada em arquivos isolados em uma estrutura de análise centralizada.

### Antes

```text
Arquivos Excel
     │
     ├── Vendas 2020
     ├── Vendas 2021
     ├── Vendas 2022
     ├── Devoluções
     └── Clientes
            │
            ▼
      Análises manuais
```

### Depois

```text
             Fontes de dados
                    │
                    ▼
             Power Query
                    │
                    ▼
             Modelo analítico
                    │
                    ▼
              Medidas DAX
                    │
                    ▼
            Power BI Dashboard
                    │
                    ▼
            Análise e decisão
```

A principal entrega do projeto, portanto, não é apenas a construção de gráficos, mas a criação de uma **solução de Business Intelligence orientada a um problema de negócio**, permitindo transformar dados operacionais em informações para tomada de decisão.

---

## 👨‍💻 Autor

**Daniel Martins França**

***Projeto desenvolvido como parte do portfólio de **Business Intelligence e Análise de Dados**, com foco em modelagem, tratamento de dados, criação de indicadores e visualização utilizando Power BI.***
