# 📊 Dashboard CSV Interativo

Sistema simples em Python desenvolvido com **Streamlit** e **Pandas** para leitura dinâmica de arquivos CSV e geração automática de indicadores e gráficos.

---

## 🚀 Funcionalidades

* **Upload Interativo:** Permite que o operador envie qualquer arquivo CSV diretamente pela interface ou utilize um arquivo padrão local.
* **Filtros Dinâmicos:** Filtre os dados por Região e por Linha de Produto em tempo real.
* **Indicadores Principais (KPIs):** Visualização rápida de Total de Vendas, Número de Pedidos e Ticket Médio.
* **Estatísticas Descritivas Avançadas:** Seleção dinâmica de colunas numéricas para análise de Mínimo, Máximo, Média, Mediana e Desvio Padrão.
* **Gráficos Interativos (Plotly):**
  * Gráfico de barras (Vendas por Categoria).
  * Gráfico de linhas (Evolução de Vendas Mensais).
  * Gráfico de dispersão / Scatter Plot (Relação entre Quantidade de Itens e Valor de Vendas).
* **Tabela de Dados:** Visualização completa e filtrada do conjunto de dados carregado.

## 📁 Estrutura do Repositório

```text
meu-projeto-dashboard/
│
├── data/
│   └── vendas_exemplo.csv      # Arquivo CSV de exemplo com a estrutura ideal
│
├── src/
│   └── app.py                  # Script principal do Dashboard (Streamlit)
│
├── .gitignore                  # Arquivos ignorados pelo Git (venv, cache, etc.)
├── README.md                   # Documentação do projeto
└── requirements.txt            # Dependências e bibliotecas do Python
```

## 📋 Modelo Ideal de Colunas do CSV

Para que o dashboard funcione corretamente — gerando todos os KPIs, gráficos de barras, linhas, dispersão e estatísticas avançadas —, o arquivo CSV de entrada deve conter obrigatoriamente as seguintes colunas com seus respectivos tipos e formatos:

| Nome da Coluna  | Tipo de Dado     | Descrição / Exemplo                                                             | Formato Esperado            |
|-----------------|------------------|---------------------------------------------------------------------------------|-----------------------------|
| Name            | Texto (String)   | Nome do cliente ou vendedor (Ex: Ana Silva)                                     | Texto livre                 |
| Date            | Data (Date)      | Data da operação ou transação                                                   | AAAA-MM-DD (Ex: 2026-01-15) |
| Ticket date     | Data (Date)      | Data de emissão do ticket/fatura                                                | AAAA-MM-DD (Ex: 2026-01-15) |
| Line of Product | Texto (String)   | Categoria ou linha do produto (Ex: Eletrônicos, Roupas, Casa e Cozinha, Livros) | Texto livre                 |
| Region          | Texto (String)   | Região geográfica da venda (Ex: Sudeste, Sul, Nordeste, Centro-Oeste, Norte)    | Texto livre                 |
| Quantity        | Numérico Inteiro | Quantidade de itens vendidos por transação (Ex: 1, 2, 5)                        | Número inteiro (int)        |
| Sales           | Numérico Decimal | Valor monetário total da venda (Ex: 1250.50)                                    | Decimal com ponto (float)   |


### Dicas para os Dados:
* A primeira linha do CSV deve conter obrigatoriamente os **cabeçalhos (nomes das colunas)**.
* O sistema identifica automaticamente colunas de texto (como categorias) e colunas numéricas (como valores e quantidades) para preencher os gráficos e indicadores.

## 🚀 Como Executar o Projeto

1. Certifique-se de ter o **Python 3.10+** instalado em sua máquina.

2. Clone o repositório ou baixe os arquivos para o seu computador.

3. Abra o terminal na pasta raiz do projeto e crie um ambiente virtual:
   ```bash
   python -m venv venv
   ```

4. Ative o ambiente virtual:
   * **Windows:** `venv\Scripts\activate`
   * **Mac/Linux:** `source venv/bin/activate`

5. Instale as dependências necessárias:
   ```bash
   pip install -r requirements.txt
   ```

6. Execute o aplicativo Streamlit:
   ```bash
   streamlit run src/app.py
   ```

7. O navegador abrirá automaticamente com o dashboard. Utilize o painel lateral para fazer o upload do seu arquivo CSV formatado.

## 🛠️ Tecnologias Utilizadas

- Python: Linguagem base de programação.

- Pandas: Manipulação, limpeza e agregação dos dados do CSV.

- Streamlit: Construção rápida e elegante da interface web interativa do dashboard.

- Plotly: Biblioteca para renderização de gráficos interativos e responsivos.
